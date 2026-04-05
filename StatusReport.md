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
- The salary dataset is easier to load and clean
- The FBref dataset requires more formatting depending on the table
We have succesfully inspected columns and confirmed key variables. We have completed the cleaning & preprocessing in Python and our processed datasets can be found here: (LINK HERE). For the FBref dataset text fields such as player names and club names were cleaned by trimming whitespace and converting values to a consistent lowercase format. Numeric variables (such as minutes, goals, and assists) were converted from string format to numeric values to allow for analysis.
Additionally, rows that did not represent valid players (such as headers or placeholder rows like “squad”) were removed. In cases where players appeared multiple times due to transfers between clubs, duplicates were resolved by keeping the observation with the highest minutes played, representing the player’s primary team for the season. The salary dataset required standardization of column names and formatting. First and last name fields were combined into a single full player name variable to match the structure of the statistics dataset. Salary fields, which were originally formatted as strings with dollar signs and commas, were cleaned and converted into numeric values. Similar to the statistics dataset, text fields were standardized by removing extra whitespace and converting values to lowercase. Non-relevant entries such as “MLS pool,” “retired,” and “without a club” were removed, since these players could not be matched to performance data. Moreover, to clean both datasets we had to make a new pool of club names to erase differences in club names and ensure the names used in both datasets matched.
Despite our efforts, some players could not be matched due to differences in naming conventions or data availability. This is expected when working with real-world datasets from different sources.
However, we want to use the new tool shown in class "OpenRefine" to redo our preprocessing to double check our work with another platform.

## 3. Merge Datasets
**Status: In progress (Next step)**
We identified merge keys:
- Player name
- Club
However, we have not finalized our merged dataset because we want to compare the one we currenlty have with another one we plan on doing with OpenRefine. Our in progress merged dataset is here: (LINK)

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
**Status: Not Started**
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



