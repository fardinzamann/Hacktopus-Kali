import socket

def port_scan(target):
    print(f"\n Scanning {target} for open ports...\n")

    for port in range(1, 65536):  #all ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  

        if sock.connect_ex((target, port)) == 0: 
            print(f" Port {port} is OPEN")
        
        sock.close() 

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    port_scan(target_ip)

