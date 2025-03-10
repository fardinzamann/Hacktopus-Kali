import subprocess
import re
import random
import time

def get_current_mac(interface):
    """Returns the current MAC address of the network interface."""
    ifconfig_result = subprocess.check_output(["ifconfig", interface], encoding="utf-8")
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Couldn't read MAC address.")
        return None

def change_mac(interface):
    """Changes the MAC address of the network interface to a random one."""
    print(f"⚙ Changing MAC address for {interface}...")

    # Generate a random MAC address (format: XX:XX:XX:XX:XX:XX)
    random_mac = ":".join([random.choice('0123456789ABCDEF') + random.choice('0123456789ABCDEF') for _ in range(6)])

    # Change the MAC address using subprocess
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", random_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

    print(f"✅ MAC address for {interface} changed to {random_mac}")
    return random_mac

def automate_mac_change(interface, num_changes=2, delay=3):
    """Automatically changes MAC address a given number of times with a delay in between."""
    for i in range(num_changes):
        print(f"\n🔄 Changing MAC address {i+1}/{num_changes}...")
        current_mac = get_current_mac(interface)
        print(f"Current MAC: {current_mac}")
        time.sleep(delay)  # Wait for a short delay between changes
        change_mac(interface)
        time.sleep(delay)  # Wait before the next change

def main():
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    print(f"Current MAC address of {interface}: {get_current_mac(interface)}")

    change = input("Do you want to automatically change the MAC address 2 times? (y/n): ")
    if change.lower() == "y":
        automate_mac_change(interface)
    else:
        print("👋 Exiting...")

if __name__ == "__main__":
    main()

