# bitcoin_tracker.py
import requests
import time
import psycopg2
import os
from datetime import datetime

# יוצרים חיבור למסד נתונים (אם לא קיים, הוא ייווצר לבד)
while True:
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "db"),
            database=os.environ.get("DB_NAME", "bitcoin"),
            user=os.environ.get("DB_USER", "user"),
            password=os.environ.get("DB_PASSWORD", "pass")
        )
        break  # אם הצליח, לצאת מהלולאה
    except psycopg2.OperationalError as e:
        print("⏳ Waiting for database to be ready...")
        time.sleep(5)
cursor = conn.cursor()

# יוצרים טבלה בשם prices אם היא עדיין לא קיימת
cursor.execute("""
    CREATE TABLE IF NOT EXISTS prices (
        timestamp TEXT,
        price REAL
    )
""")
conn.commit()
print("✅ Database connected and table created (if not existed)")

# פונקציה שמביאה את ערך הביטקוין מהאינטרנט
def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        price = response.json()["bitcoin"]["usd"]
        return price
    except Exception as e:
        print(f"שגיאה בקבלת המחיר: {e}")
        return None

# פונקציה שמחזירה ממוצע, מקסימום ומינימום
def get_stats():
    cursor.execute("SELECT price FROM prices")
    prices = [row[0] for row in cursor.fetchall()]
    if prices:
        return max(prices), min(prices), sum(prices)/len(prices)
    return 0, 0, 0

# לולאה שרצה כל 60 שניות (כל דקה)
while True:
    price = get_bitcoin_price()
    if price:
        now = datetime.now().isoformat()
        cursor.execute("INSERT INTO prices (timestamp, price) VALUES (%s, %s)", (now, price))
        conn.commit()
        print(f"📊 {now} - נרשם מחיר ביטקוין חדש: ${price}")

        max_p, min_p, avg_p = get_stats()
        action = "קנייה" if price < avg_p else "מכירה"
        print(f"🔍 מחיר נוכחי: ${price:.2f} | מקס: ${max_p:.2f} | מינ': ${min_p:.2f} | ממוצע: ${avg_p:.2f}")
        print(f"👉 המלצה: {action}")
    else:
        print("🚫 לא הצלחנו למשוך מחיר כרגע")

    time.sleep(60)  # לחכות דקה
