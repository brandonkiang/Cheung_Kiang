rule run_all:
    input:
        "visualizations/analysis_visualizations.png"

rule acquire_data_basketball:
    output:
        "data/cbb_records_2019_2024.csv",
        "data/wcbb_records_2019_2024.csv"
    shell:
        "python scripts/Athletics_Data_Acquisition.py"

rule acquire_data_academics:
    output:
        "data/scorecard.csv"
    shell:
        "python scripts/Scorecard_Data_Acquisition.py"

rule clean_data_basketball:
    input:
        "data/cbb_records_2019_2024.csv",
        "data/wcbb_records_2019_2024.csv"
    output:
        "cleaned_data/cleaned_college_basketball.csv"
    shell:
        "python scripts/Athletic_Cleaning.py"

rule clean_data_academics:
    input:
        "data/scorecard.csv"
    output:
        "cleaned_data/scorecard_cleaned.csv"
    shell:
        "python scripts/Scorecard_Cleaning.py"

rule data_integration:
    input:
        "cleaned_data/scorecard_cleaned.csv",
        "cleaned_data/cleaned_college_basketball.csv"
    output:
        "cleaned_data/integrated_data.csv"
    shell:
        "python scripts/Integration.py"

rule data_analysis:
    input:
        "cleaned_data/integrated_data.csv"
    output:
        "visualizations/analysis_visualizations.png"
    shell:
        "python scripts/Analysis.py"