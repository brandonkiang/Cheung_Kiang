import requests
import pandas as pd
import time
import os
from io import StringIO

def scrape_cbb_data(start_year, end_year, gender="men"):
    all_records = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for year in range(start_year, end_year + 1):
        print(f"Scraping {gender} {year}...")
        
        stats_url = f"https://www.sports-reference.com/cbb/seasons/{gender}/{year}-school-stats.html"
        response = requests.get(stats_url, headers=headers)
        
        clean_html = response.text.replace('<!--', '').replace('-->', '')
        
        try:
            df_year = pd.read_html(StringIO(clean_html), match="School")[0]
            df_year['Year'] = year
            all_records.append(df_year)
        except Exception as e:
            print(f"  -> Error finding stats table for {year}: {e}")

        time.sleep(15) 

    final_records = pd.concat(all_records, ignore_index=True) if all_records else pd.DataFrame()
    
    return final_records

if not os.path.exists("data"):
    os.makedirs("data")

records = scrape_cbb_data(2019, 2024, "men")
records_w = scrape_cbb_data(2019, 2024, "women")

records.to_csv("data/cbb_records_2019_2024.csv", index=False)
records_w.to_csv("data/wcbb_records_2019_2024.csv", index=False)