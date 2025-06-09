# Bitcoin Tracker

Bitcoin Tracker is a simple Python-based application that fetches and displays the current Bitcoin price using a public API.  
This project includes infrastructure automation with Ansible to streamline deployment using Docker.

---

## 📁 Project Structure

bitcoin-tracker/
├── README.md
├── ansible/
│ ├── inventory
│ ├── roles/
│ │ └── deploy_app/
│ │ └── tasks/
│ │ └── main.yml
│ └── site.yml
└── bitcoin-tracker/
├── Dockerfile
├── bitcoin_tracker.py
├── docker-compose.yml
└── requirements.txt

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the repository

Make sure Git is installed, then run:

```bash
git clone https://github.com/YOUR_USERNAME/bitcoin-tracker.git
cd bitcoin-tracker
Replace YOUR_USERNAME with your actual GitHub username if public.

2. Install Ansible
You can install Ansible with:

bash
Copy
Edit
sudo apt update
sudo apt install ansible -y
On Amazon Linux or CentOS, use yum instead of apt.

3. Run the Ansible Playbook
To deploy the app using Ansible:

bash
Copy
Edit
ansible-playbook -i ansible/inventory ansible/site.yml
This will build and run the application using the Docker setup.

🐳 Docker Notes
The app is containerized using both Dockerfile and docker-compose.yml.

The Ansible role deploy_app automates the deployment via Docker.

📬 Contact
If you have any questions or suggestions, feel free to open an issue or contact the maintainer.

