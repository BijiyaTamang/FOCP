import sys
import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Website at {url} is reachable and working.")
        else:
            print(f"Website at {url} returned a status code of {response.status_code}.")
    except requests.ConnectionError:
        print(f"Website at {url} is not reachable.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        check_website(sys.argv[1])
