import os

#Port Scanner
def run_port_scanner():
    os.system("python3 port_scanner.py")

#Vulnerability Scanner
def run_web_vuln_scanner():
    os.system("python3 web_vuln_scanner.py")

#Keylogger
def run_keylogger():
    os.system("python3 keylogger.py")

#MAC
def run_mac_changer():
    os.system("python3 mac_address_changer.py")

#Exploit Scanner
def run_exploit_scanner():
    os.system("python3 exploit_scanner.py")

#Brute Force
def run_brute_force_tester():
    os.system("python3 brute_force_tester.py")
    
    
def run_wifi_deauthenticator():
    os.system("python3 wifi_deauthenticator.py")
    
def run_osint_tool():
    os.system("python3 osint_tool.py")

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
        print("8️⃣ Automated OSINT Tool")
        print("9️⃣ Exit")

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
            run_wifi_deauthenticator()
        elif choice == "8":
            run_osint_tool()
        elif choice == "9":
            print("👋 Exiting Hacktopus-Kali...")
            break
        else:
            print("⚠ Invalid option! Try again.")

if __name__ == "__main__":
    main()
