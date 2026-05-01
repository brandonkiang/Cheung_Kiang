import pandas as pd
import os


mbb = pd.read_csv("../data/cbb_records_2019_2024.csv", header = 1)
mbb.drop(["Unnamed: 8_level_1", "Unnamed: 11_level_1", "Unnamed: 14_level_1", "Unnamed: 17_level_1", "Unnamed: 20_level_1"], axis=1, inplace=True)
mbb.rename(columns = {"W.1": "Conference_Wins", "L.1" : "Conference_Losses", "W.2": "Home_wins", "L.2": "Home_losses", "W.3": "Away_wins", "L.3": "Away_losses", "Unnamed: 38": "Year"}, inplace=True)

mbb = mbb[mbb.Rk.isna() == False]
mbb = mbb[mbb.Conference_Wins != "W"]

mbb["School"] = mbb["School"].str.lower().str.strip()
mbb["Gender"] = "Male"


wcbb = pd.read_csv("../data/wcbb_records_2019_2024.csv", header=1)
wcbb.drop(["Unnamed: 8_level_1", "Unnamed: 11_level_1", "Unnamed: 14_level_1", "Unnamed: 17_level_1", "Unnamed: 20_level_1"], axis=1, inplace=True)
wcbb.rename(columns = {"W.1": "Conference_Wins", "L.1" : "Conference_Losses", "W.2": "Home_wins", "L.2": "Home_losses", "W.3": "Away_wins", "L.3": "Away_losses", "Unnamed: 38": "Year"}, inplace=True)

wcbb = wcbb[wcbb.Rk.isna() == False]
wcbb = wcbb[wcbb.Conference_Wins != "W"]

wcbb["School"] = wcbb["School"].str.lower().str.strip()
wcbb["Gender"] = "Female"

records_combined = pd.concat([mbb, wcbb]).reset_index(drop = True)


cbb_champs = pd.read_csv("../data/cbb_champions_2019_2024.csv")
cbb_champs["Conference"] = cbb_champs["Conference"].str.lower().str.strip()
cbb_champs["Regular Season Champ"] = cbb_champs["Regular Season Champ"].str.lower().str.strip()
cbb_champs["Tournament Champ"] = cbb_champs["Tournament Champ"].str.lower().str.strip()
cbb_champs["Gender"] = "Male"


wcbb_champs = pd.read_csv("../data/wcbb_champs_2019_2024.csv")
wcbb_champs["Conference"] = wcbb_champs["Conference"].str.lower().str.strip()
wcbb_champs["Regular Season Champ"] = wcbb_champs["Regular Season Champ"].str.lower().str.strip()
wcbb_champs["Tournament Champ"] = wcbb_champs["Tournament Champ"].str.lower().str.strip()
wcbb_champs["Gender"] = "Female"

champs_combined = pd.concat([cbb_champs, wcbb_champs]).reset_index(drop = True)


tournament_champ = []
regular_season_champ = []

for i in range(len(records_combined)):
    tourney_champ = 0
    season_champ = 0
    for j in range(len(champs_combined)):
        if records_combined.Year[i] == champs_combined.Year[j]:
            if records_combined.Gender[i] == champs_combined.Gender[j]:
                school = records_combined.School[i].replace("\xa0ncaa", "")
                if school == champs_combined["Tournament Champ"][j]:
                    tourney_champ = 1
                if school in str(champs_combined["Regular Season Champ"][j]):
                    season_champ = 1
    
    tournament_champ.append(tourney_champ)
    regular_season_champ.append(season_champ)

cleaned_data = records_combined.copy()
cleaned_data["Conference_Tournament_Champion"] = tournament_champ
# cleaned_data["Conference Regular Season Champion"] = regular_season_champ

if not os.path.exists("cleaned_data"):
    os.makedirs("cleaned_data")

cleaned_data.to_csv("cleaned_data/cleaned_college_basketball.csv", index=False)