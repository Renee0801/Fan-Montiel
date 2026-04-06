# Status Report: MLS Player Performance and Salary Analysis
## Overview
Our project analyzes whether player salary in Major League Soccer relects measureable on field performance. We are integrating two public datasets: 2025 MLS player statistics from FBref and player compensation data from the MLS Players Association Salary Guide. The goal is to determine whether high paid players tend to produce stronger statistical outputs, identify which performance variables are most associated with compensation, and explore whether some players appear overpaid or underpaid relative to production. Since completing Milestone 2 we have made progress on data preparation and identified key challenges such as mismatched player names and differences in dataset formats.
This report outlines our progress on each planned task, updates our timeline, explains any changes to our project plan, and describes challenges we have encountered so far.

## Status of Planned Tasks
### 1. Finalize research questions
**Status: Complete**
We finalized our research questions from Milestone 2:
- Do higher-paid MLS players produce stronger performance statistics?
- Which performance metrics are most associated with salary?
- Are some players overpaid or underpaid?
- How efficiently do MLS teams convert salary into performance?

These questions remain unchanged and clearly align with our datasets.

## 2. Clean and Preprocess data
**Status: Complete**
We began loading both datasets into Python using Pandas.
- We cleaned the MLSPA salary dataset in Python and prepared it for later analysis. The raw file contained salary values stored as text, separate first and last name fields, and several non player entries.Our cleaning process included: combining first and last names into one player name field, standardizing text fields, removing non player entries, converting salary columns to numeric values, standardizing team names. The cleaned dataset can be found here: /data/processed/salary_cleaned.csv
- The FBref dataset requires more formatting depending on the table
We have succesfully inspected columns and confirmed key variables. We have completed the cleaning & preprocessing in Python and our processed datasets can be found in the jupyter notebook in our tag (cell #45 & 46). For the FBref dataset text fields such as player names and club names were cleaned by trimming whitespace and converting values to a consistent lowercase format. Numeric variables (such as minutes, goals, and assists) were converted from string format to numeric values to allow for analysis.
Additionally, rows that did not represent valid players (such as headers or placeholder rows like “squad”) were removed. In cases where players appeared multiple times due to transfers between clubs, duplicates were resolved by keeping the observation with the highest minutes played, representing the player’s primary team for the season. The salary dataset required standardization of column names and formatting. First and last name fields were combined into a single full player name variable to match the structure of the statistics dataset. Salary fields, which were originally formatted as strings with dollar signs and commas, were cleaned and converted into numeric values. Similar to the statistics dataset, text fields were standardized by removing extra whitespace and converting values to lowercase. Non-relevant entries such as “MLS pool,” “retired,” and “without a club” were removed, since these players could not be matched to performance data. Moreover, to clean both datasets we had to make a new pool of club names to erase differences in club names and ensure the names used in both datasets matched.
Despite our efforts, some players could not be matched due to differences in naming conventions or data availability. This is expected when working with real-world datasets from different sources.
However, we want to use the new tool shown in class "OpenRefine" to redo our preprocessing to double check our work with another platform.

## 3. Merge Datasets
**Status: In progress (Next step)**
We identified merge keys:
- Player name
- Club
However, we have not finalized our merged dataset because we want to compare the one we currenlty have with another one we plan on doing with OpenRefine. Our in progress merged dataset is found in our jupyter notebook in cell #47. Notebook can be found in our tag as is labeled "Dataset Work".

## 4. Create Derived Variables
**Status: Partially started**
We defined the variables we want to create:
- Goal contributions = Goals + Assists
- Goals per 90
- Salary per goal contribution
Implementation has started in python but is not complete.

## 5. Exploratory Data Analysis
**Status: Not Started**
We have not yet completed Exploratory Data Analysis since the merged dataset is not yet finished.
However we plan to make these visuals:
- Salary vs goal contribution scatter plot
- Distribution of Salaries
- Distribution of performance metrics

## 6. Correlation and Regression Analysis
**Status: Not Started (Preparation completed)**
This will be completed after Exploratory Data Analysis and finalized dataset merging.

## Updated Timeline:

## Complete
- Finalized research questions
- Cleaned both datasets in Python (names, clubs, and stats have been standardized)
- Preliminary merged dataset is complete

## Next Steps (Next week)
- Redo merging of datatsets with OpenRefine and compare with preliminary merged set
- Add derived variables into finalized merged dataset
## Final phase
- Perform exploratory analysis
- Create visualizations
- Run correlation and regression
- Write final report

## Challenges and Solutions
### 1. Player name mismatches  
Different formats between datasets (full name vs split names)
**Solution:**
- Standardize names  
- Trim whitespace  
- Combine first and last names  
- Manually verify mismatches
- 
### 2. Club naming inconsistencies  
Example: slight formatting differences in team names  
**Solution:**
- Create a map to standardize team names

### 3. Performance differences by position  
Defenders don’t accumulate goals/assists like attackers  
**Solution:**
- Acknowledge as limitation  
- Potentially focus analysis on attacking players

## Changes to Project Plan  
While our core research questions remain unchanged, we made minor adjustments to our workflow based on progress so far. Specifically, we decided to reprocess and validate our dataset merging using OpenRefine in addition to Python to improve data quality and matching accuracy. This adjustment was made after encountering inconsistencies in player names and club identifiers across datasets.

## Team Member Contributions:
### Gil Montiel
For this milestone, I focused primarily on data preparation and integration. I cleaned the FBref statistics dataset by removing duplicate columns, selecting relevant variables, and converting data types for analysis. I also standardized player and club names, including handling inconsistencies such as abbreviations, formatting differences, and special characters.

In addition, I led the dataset integration process by identifying appropriate merge keys and resolving mismatches between the two datasets. This included creating mappings for inconsistent team names and applying cleaning functions to improve player name matching. I also began implementing feature engineering variables such as goal contributions and goals per 90 minutes.

Finally, I contributed to debugging and refining the workflow in Python to ensure the merged dataset was accurate and usable for analysis.

### Ruilin Fan
For this milestone, I focused on cleaning and preparing the MLSPA salary dataset. I processed the raw salary data by combining first and last name fields into a single player identifier and standardizing text fields such as player names, team names, and positions by trimming whitespace and converting values to lowercase. I also converted salary-related variables (base salary and guaranteed compensation) from string format into numeric values by removing formatting characters such as dollar signs and commas. Additionally, I removed non-player entries such as "MLS pool," "retired," and "without a club" to ensure the dataset could be accurately merged with performance data.

I also assisted in planning the exploratory data analysis phase by identifying relevant variables and potential visualizations, such as salary distributions and performance efficiency metrics. Finally, I contributed to documenting the workflow and writing sections of this report to ensure clarity and completeness.

### Collaborative Work
Both team members worked together to:

- refine and confirm research questions  
- identify key challenges in merging real-world datasets  
- design the data cleaning and integration workflow  
- evaluate the quality of the merged dataset  
- plan the next steps for exploratory data analysis and modeling  

This collaborative effort ensured that both the technical and analytical aspects of the project are aligned moving forward.






