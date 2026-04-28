import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment
import time

def scrape_cbb_data(start_year, end_year):
    all_records = []
    all_champions = []

    for year in range(start_year, end_year + 1):
        print(f"Scraping {year}...")

        stats_url = f"https://www.sports-reference.com/cbb/seasons/men/{year}-school-stats.html"
        response = requests.get(stats_url)
        
        try:
            df_year = pd.read_html(response.text, attrs={'id': 'basic_school_stats'})[0]
            df_year['Year'] = year
            all_records.append(df_year)
        except Exception:
            soup = BeautifulSoup(response.text, 'html.parser')
            placeholder = soup.find('div', {'id': 'all_basic_school_stats'})
            if placeholder:
                comment = placeholder.find(string=lambda text: isinstance(text, Comment))
                df_year = pd.read_html(str(comment))[0]
                df_year['Year'] = year
                all_records.append(df_year)

        summary_url = f"https://www.sports-reference.com/cbb/seasons/men/{year}.html"
        summ_response = requests.get(summary_url)
        try:
            df_conf = pd.read_html(summ_response.text, attrs={'id': 'conference-summary'})[0]
            df_conf['Year'] = year
            all_champions.append(df_conf)
        except:
            pass

        time.sleep(7)

    final_records = pd.concat(all_records, ignore_index=True)
    final_champs = pd.concat(all_champions, ignore_index=True)
    
    return final_records, final_champs

records, champs = scrape_cbb_data(2019, 2024)
records.to_csv("../data/cbb_records_2019_2024.csv", index = False)
champs.to_csv("../data/cbb_champions_2019_2024.csv", index = False)

def scrape_wcbb_data(start_year, end_year):
    all_records = []
    all_champions = []

    for year in range(start_year, end_year + 1):
        print(f"Scraping {year}...")
        
        stats_url = f"https://www.sports-reference.com/cbb/seasons/women/{year}-school-stats.html"
        response = requests.get(stats_url)
        
        try:
            df_year = pd.read_html(response.text, attrs={'id': 'basic_school_stats'})[0]
            df_year['Year'] = year
            all_records.append(df_year)
        except Exception:
            soup = BeautifulSoup(response.text, 'html.parser')
            placeholder = soup.find('div', {'id': 'all_basic_school_stats'})
            if placeholder:
                comment = placeholder.find(string=lambda text: isinstance(text, Comment))
                df_year = pd.read_html(str(comment))[0]
                df_year['Year'] = year
                all_records.append(df_year)

        summary_url = f"https://www.sports-reference.com/cbb/seasons/women/{year}.html"
        summ_response = requests.get(summary_url)
        try:
            df_conf = pd.read_html(summ_response.text, attrs={'id': 'conference-summary'})[0]
            df_conf['Year'] = year
            all_champions.append(df_conf)
        except:
            pass

        time.sleep(7)

    final_records = pd.concat(all_records, ignore_index=True)
    final_champs = pd.concat(all_champions, ignore_index=True)
    
    return final_records, final_champs

records_w, champs_w = scrape_wcbb_data(2019, 2024)
records_w.to_csv("../data/wcbb_records_2019_2024.csv", index = False)
champs_w.to_csv("../data/wcbb_champs_2019_2024.csv", index = False)