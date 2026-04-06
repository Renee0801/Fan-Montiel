import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/MLS_Salary_2025_Fall_Release.csv")

# 1. Combine player names
df["player_name"] = df["First Name"].str.strip() + " " + df["Last Name"].str.strip()

# 2. Standardize text fields
df["player_name"] = df["player_name"].str.lower().str.strip()
df["Team Name"] = df["Team Name"].str.lower().str.strip()
df["Position"] = df["Position"].str.lower().str.strip()

# 3. Remove non-player entries
remove_values = ["mls pool", "retired", "without a club"]
df = df[~df["Team Name"].isin(remove_values)]

# 4. Clean salary columns
def clean_salary(x):
    if pd.isna(x):
        return None
    return float(str(x).replace("$", "").replace(",", "").strip())
df["base_salary"] = df["Base Salary"].apply(clean_salary)
df["guaranteed_compensation"] = df["Guaranteed Compensation"].apply(clean_salary)

# 5. Select relevant columns
df_clean = df[[
    "player_name",
    "Team Name",
    "Position",
    "base_salary",
    "guaranteed_compensation"
]]

# 6. Save cleaned dataset
df_clean.to_csv("data/processed/salary_cleaned.csv", index=False)
print("Salary dataset cleaned and saved successfully.")
