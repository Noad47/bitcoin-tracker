
# 🪙 Bitcoin Tracker with Docker & Ansible

This project tracks the current Bitcoin value from a public REST API every 1 minute, stores the values in a database, and provides stats like **min**, **max**, and **average**. Based on the latest value, it recommends whether to **buy** or **sell**.

All components run inside Docker containers. Bonus features include Ansible automation.

---

## 📦 Features

- Fetches Bitcoin price every minute from a REST API
- Stores results in a database (PostgreSQL)
- Calculates min, max, and average price from start
- Gives buy/sell recommendation after each update
- Dockerized solution (multi-container support)
- Ansible Playbook for full setup automation
> 💡 You can modify the `inventory` file inside the `ansible/` directory to apply the configuration to additional remote servers.

---

## 🚀 Quick Start Guide
### 1. Install Git

```bash
# Install Git (choose the command according to your operating system):

# For Amazon Linux / CentOS / RHEL:
sudo yum update -y
sudo yum install -y git

# For Debian / Ubuntu:
sudo apt update
sudo apt install -y git
```
### 2. Clone the Repository

```bash
# Clone the repository:
git clone https://github.com/Noad47/bitcoin-tracker.git
cd bitcoin-tracker
```

### 3. Install Ansible (if not already installed)

```bash
# For Amazon Linux / CentOS / RHEL:
sudo yum install -y ansible

# For Debian / Ubuntu:
sudo apt update
sudo apt install -y ansible
```

### 4. Run the Ansible Playbook

```bash
ansible-playbook -i ansible/inventory ansible/site.yml
```

> This will install Docker runtime (if needed), build the containers, and run the full system.

---

## 🐳 Docker Architecture

- `bitcoin-fetcher`: Pulls BTC prices and logs stats
- `db`: Database to store the prices (PostgreSQL)

All services are orchestrated with Docker Compose.

---

## 📁 Project Structure

```
├── bitcoin-tracker 
│   ├── README.md
│   ├── ansible
│   │   ├── inventory
│   │   ├── roles
│   │   │   └── deploy_app
│   │   │       └── tasks
│   │   │           └── main.yml
│   │   └── site.yml
│   └── bitcoin-tracker
│       ├── Dockerfile
│       ├── bitcoin_tracker.py
│       ├── docker-compose.yml
│       └── requirements.txt
```

---

## 📈 Sample Output

```bash
2025-06-09T13:37:08.006704 - New Bitcoin price recorded: $107648
 Current: $107648.00 | Max: $107648.00 | Min: $107637.00 | Avg: $107642.50
Recommendation: Sell
```

### 🔍 View Live Logs

You can monitor the logs using the following method:

```bash
sudo docker logs -f bitcoin-tracker
```

---

## ✅ Requirements

- Git
- Ansible
- Docker (installed by Ansible if missing)

---
