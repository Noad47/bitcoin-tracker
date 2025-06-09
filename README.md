
# 🪙 Bitcoin Tracker with Docker & Ansible

This project tracks the current Bitcoin value from a public REST API every 1 minute, stores the values in a database, and provides stats like **min**, **max**, and **average**. Based on the latest value, it recommends whether to **buy** or **sell**.

All components run inside Docker containers. Bonus features include Ansible automation.

---

## 📦 Features

- Fetches Bitcoin price every minute from a REST API
- Stores results in a database (SQLite/PostgreSQL/etc.)
- Calculates min, max, and average price from start
- Gives buy/sell recommendation after each update
- Dockerized solution (multi-container support)
- Ansible Playbook for full setup automation

---

## 🚀 Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install Ansible (if not already installed)

**Debian/Ubuntu:**
```bash
sudo apt update
sudo apt install ansible -y
```

**macOS (with Homebrew):**
```bash
brew install ansible
```

### 3. Run the Ansible Playbook

```bash
ansible-playbook -i ansible/inventory ansible/site.yml
```

> This will install Docker runtime (if needed), build the containers, and run the full system.

---

## 🐳 Docker Architecture

- `bitcoin-fetcher`: Pulls BTC prices and logs stats
- `db`: Database to store the prices (SQLite/PostgreSQL)
- `logger`: (Optional) logs to a file or dashboard

All services are orchestrated with Docker Compose.

---

## 📁 Project Structure

```
.
├── ansible/
│   ├── inventory
│   └── site.yml
├── docker/
│   └── Dockerfiles and configs
├── src/
│   └── fetcher.py
├── README.md
└── docker-compose.yml
```

---

## 📈 Sample Output

```bash
[INFO] Current BTC: 67,234.45 USD
[INFO] Min: 66,980.12 | Max: 67,234.45 | Avg: 67,101.98
[RECOMMENDATION] SELL
```

---

## ✅ Requirements

- Git
- Ansible
- Docker (installed by Ansible if missing)

---

## 📬 Contributions

Feel free to fork, improve, or raise issues via [GitHub Issues](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/issues).


Ansible

Docker (installed by Ansible if missing)

📬 Contributions
Feel free to fork, improve, or raise issues via GitHub Issues.
