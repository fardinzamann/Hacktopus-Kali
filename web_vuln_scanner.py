import requests
from urllib.parse import urlparse

def check_http_status(target):
    print(f" Checking HTTP status for {target}...")
    try:
        response = requests.get(target)
        print(f" HTTP Status: {response.status_code}")
        
        if response.status_code == 200:
            print(f" Website is accessible and responding!")
        elif response.status_code == 404:
            print(f" Page not found (404)!")
        else:
            print(f" Unexpected status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" Error occurred: {e}")

def check_sql_injection(target):
    print("\n Checking for SQL Injection vulnerabilities...")
    payloads = ["' OR 1=1 --", "' OR 'a'='a", "' OR 1=1#", "admin' --", "admin' #"]
    for payload in payloads:
        url = target + payload
        try:
            response = requests.get(url)
            if "error" in response.text.lower():
                print(f"Potential SQL Injection detected with payload: {payload}")
        except requests.exceptions.RequestException as e:
            print(f" Error occurred with payload {payload}: {e}")

def check_xss(target):
    print("\n Checking for XSS vulnerabilities...")
    payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>", "<a href='javascript:alert(1)'>Click me</a>"]
    for payload in payloads:
        url = target + payload
        try:
            response = requests.get(url)
            if payload in response.text:
                print(f" Potential XSS vulnerability detected with payload: {payload}")
        except requests.exceptions.RequestException as e:
            print(f" Error occurred with payload {payload}: {e}")

def check_security_headers(target):
    print("\n Checking HTTP security headers...")
    headers = ['Strict-Transport-Security', 'X-Content-Type-Options', 'Content-Security-Policy', 'X-Frame-Options']
    try:
        response = requests.head(target)
        for header in headers:
            if header not in response.headers:
                print(f"Missing security header: {header}")
            else:
                print(f"Security header {header} is present")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred checking headers: {e}")

def check_sensitive_data_exposure(target):
    print("\n Checking for sensitive data exposure...")
    if target.startswith("http://"):
        print(f"Warning: Sensitive data might be exposed over HTTP, consider using HTTPS.")
    else:
        print(f"Website is using HTTPS.")

# Function to start scanning
def scan(target):
    check_http_status(target)
    check_sql_injection(target)
    check_xss(target)
    check_security_headers(target)
    check_sensitive_data_exposure(target)

# Main function
def main():
    target = input("Enter target URL (e.g., http://example.com): ")
    scan(target)

if __name__ == "__main__":
    main()

