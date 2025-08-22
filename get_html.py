
import requests
from bs4 import BeautifulSoup

url = "https://www.warmemo.or.kr:8443/Home/H50000/H50200/H50201/warDeadList?selection_cd=01&page=1"

try:
    response = requests.get(url, verify=False) # verify=False to handle potential SSL issues
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    with open("warmemo_page1.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Successfully fetched and saved warmemo_page1.html")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
    print("Please check your internet connection or if the website is blocking requests.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
