import os
from port_scanner import port_scan  # Import the port scanner function

def main_menu():
    while True:
        print("\n🐙 Hacktopus-Kali - Cybersecurity Toolkit 🐙\n")
        print("1️⃣ Port Scanner")
        print("2️⃣ Web Vulnerability Scanner (Coming Soon)")
        print("3️⃣ Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter target IP: ")
            port_scan(target, range(1, 1025))  # Run the port scanner on common ports
        elif choice == "3":
            print("Exiting Hacktopus-Kali...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main_menu()
