import pandas as pd
import os


mbb = pd.read_csv("data/cbb_records_2019_2024.csv", header = 1)
mbb.drop(["Unnamed: 8_level_1", "Unnamed: 11_level_1", "Unnamed: 14_level_1", "Unnamed: 17_level_1", "Unnamed: 20_level_1"], axis=1, inplace=True)
mbb.rename(columns = {"W.1": "Conference_Wins", "L.1" : "Conference_Losses", "W.2": "Home_wins", "L.2": "Home_losses", "W.3": "Away_wins", "L.3": "Away_losses", "Unnamed: 38": "Year"}, inplace=True)

mbb = mbb[mbb.Rk.isna() == False]
mbb = mbb[mbb.Conference_Wins != "W"]

mbb["School"] = mbb["School"].str.lower().str.strip()
mbb["Gender"] = "Male"


wcbb = pd.read_csv("data/wcbb_records_2019_2024.csv", header=1)
wcbb.drop(["Unnamed: 8_level_1", "Unnamed: 11_level_1", "Unnamed: 14_level_1", "Unnamed: 17_level_1", "Unnamed: 20_level_1"], axis=1, inplace=True)
wcbb.rename(columns = {"W.1": "Conference_Wins", "L.1" : "Conference_Losses", "W.2": "Home_wins", "L.2": "Home_losses", "W.3": "Away_wins", "L.3": "Away_losses", "Unnamed: 38": "Year"}, inplace=True)

wcbb = wcbb[wcbb.Rk.isna() == False]
wcbb = wcbb[wcbb.Conference_Wins != "W"]

wcbb["School"] = wcbb["School"].str.lower().str.strip()
wcbb["Gender"] = "Female"

records_combined = pd.concat([mbb, wcbb]).reset_index(drop = True)

if not os.path.exists("cleaned_data"):
    os.makedirs("cleaned_data")

records_combined.to_csv("cleaned_data/cleaned_college_basketball.csv", index=False)