import os

os.system("python scripts/clean_salary.py")
os.system("jupyter nbconvert --execute --to notebook --inplace notebooks/'Dataset work.ipynb'")
