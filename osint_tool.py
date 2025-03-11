import whois
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import shodan

def get_domain_info(domain):
    print("\n🔍 Fetching domain information...")
    w = whois.whois(domain)
    return w

def get_ip_info(ip):
    print("\n🔍 Fetching IP information...")
    geolocator = Nominatim(user_agent="OSINT_Tool")
    location = geolocator.geocode(ip)
    return location

def get_social_media_info(username):
    print(f"\n🔍 Gathering social media info for {username}...")
    social_media_urls = [
        f"https://www.twitter.com/{username}",
        f"https://www.instagram.com/{username}",
        f"https://www.linkedin.com/in/{username}"
    ]
    profile_info = {}
    
    for url in social_media_urls:
        response = requests.get(url)
        if response.status_code == 200:
            profile_info[url] = "Profile Found"
        else:
            profile_info[url] = "Profile Not Found"
    return profile_info

def get_shodan_info(ip):
    print("\n🔍 Fetching Shodan information...")
    SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        host = api.host(ip)
        return host
    except shodan.APIError as e:
        return f"Error: {e}"

def main():
    print("🎩 Hacktopus-Kali - Automated OSINT Tool")
    
    # Get user input for OSINT gathering
    choice = input("What do you want to gather information on?\n1. Domain\n2. IP Address\n3. Social Media Username\n4. Exit\n👉 Select an option: ")
    
    if choice == "1":
        domain = input("Enter domain name (e.g., example.com): ")
        domain_info = get_domain_info(domain)
        print(f"Domain Information:\n{domain_info}")
        
    elif choice == "2":
        ip_address = input("Enter IP address: ")
        ip_info = get_ip_info(ip_address)
        if ip_info:
            print(f"Geographical location: {ip_info.address}")
        else:
            print("Couldn't find location for this IP.")
            
    elif choice == "3":
        username = input("Enter social media username: ")
        social_info = get_social_media_info(username)
        print("Social Media Information:")
        for url, status in social_info.items():
            print(f"{url}: {status}")
    
    elif choice == "4":
        print("👋 Exiting OSINT Tool...")
        return

    else:
        print("⚠ Invalid option! Try again.")

if __name__ == "__main__":
    main()

