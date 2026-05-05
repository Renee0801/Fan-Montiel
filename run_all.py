import os

print("Step 1: Cleaning salary data...")
os.system("python scripts/clean_salary.py")

print("Step 2: Merging datasets...")
os.system("python scripts/merge_data.py")

print("Step 3: Running analysis...")
os.system("python scripts/analysis.py")

print("Workflow completed.")
