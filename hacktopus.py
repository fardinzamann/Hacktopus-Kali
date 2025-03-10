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
            target = input("Enter target IP address: ")
            port_scan(target)  # Call the port scanner function
        elif choice == "3":
            print("Exiting Hacktopus-Kali...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main_menu()

