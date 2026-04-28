rule acquire_data:
    output:
        "data/cbb_champions_2019_2024.csv",
        "data/cbb_records_2019_2024.csv",
        "data/wcbb_champs_2019_2024.csv",
        "data/wcbb_records_2019_2024.csv",
    shell:
        "python scripts/Athletics_Data_Acquisition.py"

rule clean_data:
    input:
        "data/cbb_champions_2019_2024.csv",
        "data/cbb_records_2019_2024.csv",
        "data/wcbb_champs_2019_2024.csv",
        "data/wcbb_records_2019_2024.csv",
    output:
        "cleaned_data/cleaned_college_basketball.csv"
    shell:
        "python scripts/Athletic_Cleaning.py