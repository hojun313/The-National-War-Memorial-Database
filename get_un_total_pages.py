import requests
from bs4 import BeautifulSoup
import math

def get_total_pages(selection_cd):
    base_url = "https://www.warmemo.or.kr:8443/Home/H50000/H50200/H50202/warDeadUnList?selection_cd="
    url = f"{base_url}{selection_cd}&page=1"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        total_count_div = soup.find('div', class_='m-guide-total type01')
        if total_count_div:
            strong_tag = total_count_div.find('strong')
            if strong_tag:
                total_records_str = strong_tag.get_text(strip=True).replace(',', '')
                total_records = int(total_records_str)
                # Assuming 10 items per page
                total_pages = math.ceil(total_records / 10)
                return total_pages
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching total pages for selection_cd={selection_cd}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred for selection_cd={selection_cd}: {e}")
        return None

print("Getting total pages for UN Navy (selection_cd=02)...")
un_navy_pages = get_total_pages('02')
print(f"UN Navy total pages: {un_navy_pages}")

print("\nGetting total pages for UN Air Force (selection_cd=03)...")
un_airforce_pages = get_total_pages('03')
print(f"UN Air Force total pages: {un_airforce_pages}")

print("\nGetting total pages for UN Marine Corps (selection_cd=04)...")
un_marine_corps_pages = get_total_pages('04')
print(f"UN Marine Corps total pages: {un_marine_corps_pages}")