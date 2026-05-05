import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned/salary_cleaned.csv")

if "goals" in df.columns and "base_salary" in df.columns:
    plt.scatter(df["goals"], df["base_salary"])
    plt.xlabel("Goals")
    plt.ylabel("Base Salary")
    plt.title("Goals vs Salary")
    plt.savefig("results/goals_vs_salary.png")

print(df.head())
