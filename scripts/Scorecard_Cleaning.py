import pandas as pd

df = pd.read_csv("data/scorecard.csv")

static_fields = [
    "id", "ope8_id", "year",
    "school.name", "school.city",
    "school.state", "school.zip", "school.main_campus",
    "school.branches", "school.ownership",
    "school.institutional_characteristics.level",
]

year_fields = [
    "admissions.admission_rate.overall",
    "admissions.sat_scores.25th_percentile.critical_reading",
    "admissions.sat_scores.75th_percentile.critical_reading",
    "admissions.sat_scores.25th_percentile.math",
    "admissions.sat_scores.75th_percentile.math",
    "admissions.act_scores.25th_percentile.cumulative",
    "admissions.act_scores.75th_percentile.cumulative",
    "admissions.test_requirements",
    "student.size",
    "cost.tuition.in_state",
    "cost.tuition.out_of_state",
    "cost.avg_net_price.public",
    "cost.avg_net_price.private",
    "aid.pell_grant_rate",
]

years = [2019, 2020, 2021, 2022, 2023, 2024]

static_cols = [f for f in static_fields if f != "year"]

year_dfs = []
for yr in years:
    year_cols = {f"{yr}.{f}": f for f in year_fields}
    existing_cols = {k: v for k, v in year_cols.items() if k in df.columns}

    temp = df[static_cols + list(existing_cols.keys())].copy()
    temp["year"] = yr
    temp = temp.rename(columns=existing_cols)
    year_dfs.append(temp)

df_long = pd.concat(year_dfs, ignore_index=True)

cols = static_fields + year_fields
df_long = df_long[[c for c in cols if c in df_long.columns]]

df_long = df_long.rename(columns={
    'year': 'year',
    'id': 'unitid',
    'ope8_id': 'opeid',
    'school.name': 'institution_name',
    'school.city': 'city', 
    'school.state': 'state',
    'school.zip': 'zip',
    'school.main_campus': 'main_campus',
    'school.branches': 'num_campuses', 
    'school.ownership': 'institution_type',
    'school.institutional_characteristics.level': 'institution_years', 
    'admissions.admission_rate.overall': 'admission_rate',
    'admissions.sat_scores.25th_percentile.critical_reading': 'SAT_reading25',
    'admissions.sat_scores.75th_percentile.critical_reading': 'SAT_reading75', 
    'admissions.sat_scores.25th_percentile.math': 'SAT_math25', 
    'admissions.sat_scores.75th_percentile.math': 'SAT_math75', 
    'admissions.act_scores.25th_percentile.cumulative': 'ACT_median25', 
    'admissions.act_scores.75th_percentile.cumulative': 'ACT_median75', 
    'admissions.test_requirements': 'test_score_req', 
    'student.size': 'num_undergrad',
    'cost.tuition.in_state': 'in_state_tuition', 
    'cost.tuition.out_of_state': 'out_state_tuition', 
    'cost.avg_net_price.public': 'avg_net_price_public', 
    'cost.avg_net_price.private': 'avg_net_price_private', 
    'aid.pell_grant_rate': 'prop_low_income'})

df_long["institution_type"] = df_long['institution_type'].map({1: 'public', 2: 'private nonprofit', 3: 'private for-profit'})

df_long["institution_years"] = df_long['institution_years'].map({1: '4-year', 2: '2-year', 3: 'Less-than-2-year'})

df_long['test_score_req'] = df_long['test_score_req'].map({1: 'Required', 2: 'Recommended', 3: 'Neither required nor recommended',
                                                           4: 'Do not know', 5: 'Considered but not required'}).fillna('Do not know')

df_long['institution_name'] = df_long['institution_name'].str.lower()
df_long['city'] = df_long['city'].str.lower()

df_long.to_csv("cleaned_data/scorecard_cleaned.csv", index=False)