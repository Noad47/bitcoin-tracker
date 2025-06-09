import requests
import time
import psycopg2
import os
from datetime import datetime

# Connect to the database
while True:
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST", "db"),
            database=os.environ.get("DB_NAME", "bitcoin"),
            user=os.environ.get("DB_USER", "user"),
            password=os.environ.get("DB_PASSWORD", "pass")
        )
        break
    except psycopg2.OperationalError:
        print("Waiting for the database to be ready...")
        time.sleep(5)

cursor = conn.cursor()

# Create the prices table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS prices (
        timestamp TEXT,
        price REAL
    )
""")
conn.commit()
print("Database connected and table created (if not existed)")

# Fetch Bitcoin price from the internet
def get_bitcoin_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        price = response.json()["bitcoin"]["usd"]
        return price
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

# Return max, min, and average from DB
def get_stats():
    cursor.execute("SELECT price FROM prices")
    prices = [row[0] for row in cursor.fetchall()]
    if prices:
        return max(prices), min(prices), sum(prices)/len(prices)
    return 0, 0, 0

# Main loop
while True:
    price = get_bitcoin_price()
    if price:
        now = datetime.now().isoformat()
        cursor.execute("INSERT INTO prices (timestamp, price) VALUES (%s, %s)", (now, price))
        conn.commit()
        print(f"{now} - New Bitcoin price recorded: ${price}")

        max_p, min_p, avg_p = get_stats()
        action = "Buy" if price < avg_p else "Sell"
        print(f" Current: ${price:.2f} | Max: ${max_p:.2f} | Min: ${min_p:.2f} | Avg: ${avg_p:.2f}")
        print(f"Recommendation: {action}")
    else:
        print("Failed to fetch Bitcoin price.")

    time.sleep(60)
