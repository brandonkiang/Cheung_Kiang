import requests
import csv
import os
import hashlib

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "apikey.txt")

with open(file_path) as f:
    api_key = f.read().strip()

BASE_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"

data_dir = os.path.join(script_dir, "..", "data")
os.makedirs(data_dir, exist_ok=True)

output_file = os.path.join(data_dir, "scorecard.csv")

years = [2019, 2020, 2021, 2022, 2023, 2024]

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

static_fields = [
    "id", "ope8_id", "school.name", "school.city",
    "school.state", "school.zip", "school.main_campus",
    "school.branches", "school.ownership",
    "school.institutional_characteristics.level",
]

all_fields = static_fields + [
    f"{yr}.{f}" for yr in years for f in year_fields
]

all_results = []
page = 0

while True:
    params = {
        "api_key": api_key,
        "fields": ",".join(all_fields),
        "per_page": 100,
        "page": page,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    results = data.get("results", [])
    if not results:
        break

    all_results.extend(results)
    total = data["metadata"]["total"]
    print(f"Fetched page {page} — {len(all_results)}/{total} schools")

    if len(all_results) >= total:
        break
    page += 1

if all_results:
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_fields)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"Saved {len(all_results)} schools to {output_file}")
else:
    print("No results found.")

def hash_csv_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

hash_scorecard = hash_csv_file("data/scorecard.csv")

if not os.path.exists("sha-256_hash_values"):
    os.makedirs("sha-256_hash_values")

with open("sha-256_hash_values/SHA-256_scorecard.txt", "w") as f:
    f.write(hash_scorecard)