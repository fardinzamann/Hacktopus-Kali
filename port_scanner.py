import socket

def get_service_name(port):
    try:
        
        return socket.getservbyport(port)
    except OSError:
    
        return None

def banner_grab(target, port):
    try:
      
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        sock.send(b'Hello\r\n')  
        
       
        banner = sock.recv(1024).decode().strip()
        return banner
    except (socket.timeout, socket.error):
        return None
    finally:
        sock.close()

def port_scan(target, start_port, end_port):
    print(f"\nScanning {target} for open ports from {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  
        
        if sock.connect_ex((target, port)) == 0:  
            print(f"Port {port} is OPEN")
            

            service_name = get_service_name(port)
            if service_name:
                print(f"  Service: {service_name}")
            

            banner = banner_grab(target, port)
            if banner:
                print(f"  Banner: {banner}")
        
        sock.close()

def main():
    target_ip = input("Enter target IP address: ")
    scan_choice = input("Do you want to scan a specific port range or all ports? (range/all): ").strip().lower()
    
    if scan_choice == "range":
        start_port = int(input("Enter starting port number: "))
        end_port = int(input("Enter ending port number: "))
        port_scan(target_ip, start_port, end_port)
    else:
      
        port_scan(target_ip, 1, 65535)

if __name__ == "__main__":
    main()
