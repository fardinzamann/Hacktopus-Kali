import os
from port_scanner import port_scan
from web_vuln_scanner import scan  # Import the advanced scan function

def main_menu():
    while True:
        print("\n🐙 Hacktopus-Kali - Cybersecurity Toolkit 🐙\n")
        print("1️⃣ Port Scanner")
        print("2️⃣ Web Vulnerability Scanner")
        print("3️⃣ Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            target = input("Enter target IP address: ")
            port_scan(target)  # Run the Port Scanner
        elif choice == "2":
            target = input("Enter target URL (e.g., http://example.com): ")
            scan(target)  # Run the advanced Web Vulnerability Scanner
        elif choice == "3":
            print("Exiting Hacktopus-Kali...")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main_menu()

