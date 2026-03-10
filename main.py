import requests

def main():
    response = requests.get("https://api.github.com")
    print("Status code:", response.status_code)
    print("Response content:", response.text)

if __name__ == "__main__":
    main()