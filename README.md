🐙 **Hacktopus-Kali** 🐙  

Hacktopus-Kali is an advanced cybersecurity toolkit designed for Kali Linux. It integrates a wide variety of penetration testing tools, automations, and security features to aid cybersecurity professionals, ethical hackers, and anyone interested in learning more about cybersecurity.
 
## **Features**  

**Port Scanner** – Scans open ports on a target system.  
**Web Vulnerability Scanner** – Detects common security flaws (SQLi, XSS, etc.).  
**Keylogger** – Logs keystrokes (for ethical testing).  
**Network Packet Sniffer** – Captures and analyzes network traffic.  
**Brute Force Login Tester** – Attempts password brute force attacks on login pages.  
**MAC Address Changer** – Changes MAC addresses for anonymity.   
**Exploit Scanner** – Scans for known exploits using `searchsploit`.   
**Wireless Network Deauthenticator** – Disconnects users from a Wi-Fi network.   
**Automated OSINT Tool** – Gathers public information about a target.  

## Requirements  
- **Operating System**: Kali Linux  
- **Python 3.x**  
- Required Libraries (install via `pip`):  
  ```bash
  pip install requests beautifulsoup4 pynput scapy cryptography

## How to Install

**Hacktopus-Kali** requires **Python 3** and several Python packages to function. Follow these steps to install the toolkit on your Kali Linux machine.

### Step 1: Clone the Repository

Clone the **Hacktopus-Kali** repository to your local machine using **Git**:

```bash
git clone https://github.com/fardinzamann/Hacktopus-Kali.git
cd Hacktopus-Kali
```

### Step 2: Install Dependencies:  
```bash
sudo apt update 
sudo apt install python3-pip
pip3 install -r requirements.txt
```

### Step 3: Shodan API Key (optional):  
For the **Shodan** tool, you'll need to create an account on [Shodan](https://www.shodan.io/) to get an API key for scanning.

## How to Use
Run Hacktopus-Kali with the following command:
```bash
cd Hacktopus-Kali
python3 hacktopus.py
```

This will launch the main menu with options to run each of the tools.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) file for details.

