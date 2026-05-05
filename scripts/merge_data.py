import pandas as pd

stats = pd.read_excel("data/raw/MLS STATS 2025.xlsx")
salary = pd.read_csv("data/raw/MLS_Salary_2025_Fall_Release_Original copy.csv")

stats["player_key"] = stats["Player"].astype(str).str.lower().str.strip()
salary["player_key"] = (
    salary["first_name"].astype(str).str.lower().str.strip()
    + " "
    + salary["last_name"].astype(str).str.lower().str.strip()
)

merged = pd.merge(stats, salary, on="player_key", how="inner")

merged.to_csv("data/cleaned/merged_dataset.csv", index=False)

print("Merged dataset saved.")
