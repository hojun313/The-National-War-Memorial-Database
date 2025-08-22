

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os

def scrape_and_save(branch_name, selection_cd, total_pages, output_dir):
    base_url = "https://www.warmemo.or.kr:8443/Home/H50000/H50200/H50202/warDeadUnList?selection_cd="
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Create directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    all_names = [] # To store only the names of all soldiers

    print(f"\nStarting to scrape {branch_name} data from {total_pages} pages...")

    for page_num in range(1, total_pages + 1):
        url = f"{base_url}{selection_cd}&page={page_num}"
        
        try:
            response = requests.get(url, headers=headers, verify=False, timeout=10)
            response.raise_for_status() # Raise an exception for HTTP errors
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            honor_list_div = soup.find('div', class_='honor_list')
            if honor_list_div:
                items = honor_list_div.find_all('a', class_='item')
                
                if not items:
                    print(f"No items found on page {page_num}. This might indicate the end of data or a change in structure.")
                
                for item in items:
                    # Extract only the name
                    name_dd = item.find('dt', string='성명').find_next_sibling('dd')
                    if name_dd:
                        all_names.append(name_dd.get_text(strip=True))
            else:
                print(f"Could not find 'honor_list' div on page {page_num}. Skipping this page.")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5) # Wait before retrying
            continue # Skip to the next iteration after waiting
        except Exception as e:
            print(f"An unexpected error occurred on page {page_num}: {e}")
            continue # Continue to the next page even if an error occurs
        
        # Add a delay to be polite to the server and avoid being blocked
        time.sleep(0.1) # Fixed delay of 0.1 seconds

        if page_num % 10 == 0:
            print(f"Scraped {page_num} pages so far. Total names collected: {len(all_names)}")

    print(f"\nScraping complete for {branch_name}. Total names collected: {len(all_names)}")

    # --- Custom Excel Formatting ---
    if all_names:
        excel_data = []
        row_data = []
        for i, name in enumerate(all_names):
            row_data.append(i + 1) # Sequential number
            row_data.append(name) # Soldier's name
            
            if len(row_data) == 20: # 10 pairs of (number, name)
                excel_data.append(row_data)
                row_data = []
        
        # Add any remaining data if the total count is not a multiple of 10
        if row_data:
            # Pad with empty strings if the last row is not full
            while len(row_data) < 20:
                row_data.append('') 
            excel_data.append(row_data)

        df = pd.DataFrame(excel_data)
        output_file = os.path.join(output_dir, f"war_dead_data_{branch_name}.xlsx")
        try:
            # Save without header and index
            df.to_excel(output_file, index=False, header=False)
            print(f"{branch_name} data successfully saved to {output_file}")
        except Exception as e:
            print(f"Error saving {branch_name} data to Excel: {e}")
    else:
        print(f"No {branch_name} data was collected.")


# --- Main execution for all UN branches ---
un_branches = [
    {'name': 'UN_NAVY', 'selection_cd': '02', 'total_pages': 51},
    {'name': 'UN_AIRFORCE', 'selection_cd': '03', 'total_pages': 127},
    {'name': 'UN_MARINE_CORPS', 'selection_cd': '04', 'total_pages': 430},
]

for branch in un_branches:
    scrape_and_save(
        branch['name'],
        branch['selection_cd'],
        branch['total_pages'],
        branch['name'] # Use branch name as output directory
    )

