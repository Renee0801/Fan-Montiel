# Workflow Documentation

## Step 1: Data Collection
Two datasets were collected:
- FBref MLS 2025 player statistics
- MLS Players Association salary data

## Step 2: Data Cleaning
Player names were standardized to improve matching across datasets.
Salary values were converted into numeric format.

Scripts used:
- scripts/clean_salary.py
- notebooks/Openrefine dataset work.ipynb

OpenRefine operation history:
- openrefine/openrefine work.json

## Step 3: Data Integration
The datasets were integrated using player names as the linking attribute.

## Step 4: Analysis and Visualization
The merged dataset was analyzed using correlation analysis and visualizations.

Notebook used:
- notebooks/Dataset work.ipynb

## Step 5: Results
Outputs and visualizations are stored in:
- results/
