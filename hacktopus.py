import os

def run_mac_changer():
    print("⚙ Running MAC Address Changer...")
    os.system("sudo python3 mac_changer.py")

def main():
    while True:
        print("\n🎩 Hacktopus-Kali - Advanced Cybersecurity Toolkit")
        print("1️⃣ Port Scanner")
        print("2️⃣ Web Vulnerability Scanner")
        print("3️⃣ Keylogger")
        print("4️⃣ MAC Address Changer")
        print("5️⃣ Exit")

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
            print("👋 Exiting Hacktopus-Kali...")
            break
        else:
            print("⚠ Invalid option! Try again.")

