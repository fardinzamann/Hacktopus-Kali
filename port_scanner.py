import socket  # Import socket library to handle network connections

def port_scan(target, ports):
    print(f"\n🔍 Scanning {target} for open ports...\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket
        sock.settimeout(1)  # Set timeout to 1 second for faster scanning

        result = sock.connect_ex((target, port))  # Try connecting to the port
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        else:
            print(f"❌ Port {port} is CLOSED")
        
        sock.close()  # Close the connection

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")  # Ask the user for an IP address
    port_range = range(1, 1025)  # Scans ports from 1 to 1024 (common ports)
    port_scan(target_ip, port_range)  # Run the port scanner
