import os

# Function to run Port Scanner
def run_port_scanner():
    os.system("python3 port_scanner.py")

# Function to run Web Vulnerability Scanner
def run_web_vuln_scanner():
    os.system("python3 web_vuln_scanner.py")

# Function to run Keylogger
def run_keylogger():
    os.system("python3 keylogger.py")

# Function to run MAC Address Changer
def run_mac_changer():
    os.system("python3 mac_address_changer.py")

# Function to run Exploit Scanner
def run_exploit_scanner():
    os.system("python3 exploit_scanner.py")

# Function to run Brute Force Login Tester
def run_brute_force_tester():
    os.system("python3 brute_force_tester.py")
    
    
def run_wifi_deauthenticator():
    os.system("python3 wifi_deauthenticator.py")

def main():
    while True:
        print("\n🎩 Hacktopus-Kali - Advanced Cybersecurity Toolkit")
        print("1️⃣ Port Scanner")
        print("2️⃣ Web Vulnerability Scanner")
        print("3️⃣ Keylogger")
        print("4️⃣ MAC Address Changer")
        print("5️⃣ Exploit Scanner")
        print("6️⃣ Brute Force Login Tester")
        print("7️⃣ Wireless Network Deauthenticator")
        print("8️⃣ Exit")

        choice = input("👉 Select an option: ")

        if choice == "1":
            os.system("python3 port_scanner.py")
        elif choice == "2":
            os.system("python3 web_vuln_scanner.py")
        elif choice == "3":
            run_keylogger()
        elif choice == "4":
            run_mac_changer()
        elif choice == "5":
            run_exploit_scanner()
        elif choice == "6":
            run_brute_force_tester()
        elif choice == "7":
            run_wifi_deauthenticator()  # Run the Wireless Network Deauthenticator
        elif choice == "8":
            print("👋 Exiting Hacktopus-Kali...")
            break
        else:
            print("⚠ Invalid option! Try again.")

if __name__ == "__main__":
    main()
