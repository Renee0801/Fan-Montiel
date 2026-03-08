# Major League Soccer Performance and Salary Analysis

## Overview
The purpose of this project is to examine if a player's salary in Major League Soccer (MLS) reflects measurable on field performance. Professional soccer teams invest a lot in their players through their salary, however salary does not always align with their production. Our project will analyze whether higher paid MLS players also produce bigger statistical outputs and whether some players appear overvalued or undervalued relative to their performance.

To answer this question we will combine two publically available datasets. The first dataset is the 2025 Major League Soccer player statistics page from FBref, which provides season level player performance data. The second dataset is the 2025 MLS Player Association Salary Guide, which provides player compensation data, including base salary and guranteed compensation. The MLSPA guide states that the 2025 data covers players under contract as of October 1, 2025 and it explains how guranteed compensation is calculated.

After collecting the data we will clean the datasets, by standardizing club names, and then merge the datasets. We will use exploratory data analysis, visualizations, correlation analysis, and regression modeling to identify relationships between player salaries and performance statistics. We will also make our own variables like goals per 90 minutes and salary per goal contribution to help us make comparisons more meaningful across players with varying playing time.

This project is desgined to demonstrate the full data lifecycle, including acquisition, cleaning, integration, analysis, documentation and reproducibility.

## Team
Gil Montiel
-  Collect and organize the FBred MLS player statistics dataset
-  Convert the players statistics data into a structured formar for analysis
-  Clean the player statistic dataset
-  Standardized player names and club names across both datasets
-  Merge statistics of both datasets using Pandas
-  Create our own metrics like goals per 90 and salary per goal contribution
-  Assist with exploratory analysis and visualizations

Ruilin Fan
- Collect and organize the MLSPA salary dataset
- Convert the salary data into a structured format for analysis
- Clean salary fields and convert compensation values into numeric format
- Verify accuracy of merged records and help resolve name mismatches
- Perform exploratory data analysis and create visualizations
- Assist with interpretation of results and written explanations
- Contribute to documentation, README preparation, and final report writing

Both team members will collaborate on research question refinement, interpretation of results, and ensuring that the final workflow is reproducible and clearly documented.

## Research / Business Questions
This project aims to answer the following questions:
1. Do higher_paid MLS players produce stronger on-field performance statistics?
2. Which performance metrics are most strongly associated with salary or guaranteed compensation?
3. Are some MLS players overpaid or underpaid relative to their production?
4. How efficiently do MLS teams convert player salary spending into on-field performance?
These questions make the project both analytical and practical since they connect performance measurement with financial decision-making.

## Datasets
### Dataset 1 - FBref 2025 MLS Player Statistics
#### Source: FBref
Link: https://fbref.com/en/comps/22/2025/stats/2025-Major-League-Soccer-Stats 
This dataset contains player-level statistics for the 2025 Major League Soccer season.FBref is a widely used public football statistics site, and the MLS 2025 stats page provides player performance information for the league.
#### Example variables
- Player name
- Squad / club
- Position
- Age
- Matches played
- Starts
- Minutes played
- Goals
- Assists
- Expected goals and expected assists depending on the selected table
This dataset represents player performance and will be used as the main source for measuring productivity.

### Dataset 2 - MLS Players Association Salary Guide
#### Source: MLS Players Association
Link: https://mlsplayers.org/resources/salary-guide
This dataset contains MLS player compensation data. The MLSPA salary guide states that the 2025 Salary Guide includes all MLS playyers under contract as of October 1, 2025 and reports both current annuaized base salary and annualized average guranteed compensation. It also explains that guaranteed compensation includes base salary plus guaranteed bonuses annualized over the term of the contract while excluding performance bonuses.
#### Example variables
- First name
- Last name
- Club
- Position
- Base salary
- Guaranteed compensation
This dataset represents player financial compensation and will be used to evaluate whether salaries align with performance.

## Dataset Integration
The two datasets will be integrated at the player level.
#### Likely shared identifiers
- Player name
- Club / squad
- Position

Because the two datasets come form different sources, some player or club names may not match perfectly. To address this, we will standardize formatting, remove extra spaces, and manually verify mismatches when needed.

The merged dataset will allow us to compare salary and performance in one file.

Integration will be performed in Python using Pandas merge operations.

## Timeline
#### Week 1
-  Finalize research questions (Gil & Ruilin)
-  Find two datasets and make sure they are analyzeable on python (Gil & Ruilin)
-  Set up file in Github and make sure it is working for both members (Gil)
-  Complete initial milestone working together (Gil & Ruilin)
-  Start inspection of variables in datasets (Gil)
#### Week 2
-  Clean and preprocess both datasets (Gil)
-  Standardize team names because datasets have small diffrences in names. For example "FC Dallas" v.s "F.C Dallas". (Gil)
-  Convert salary varibales into numbers and then merge the datasets (Ruilin)
#### Week 3
-  Conduct exploratory data analysis (Ruilin & Gil)
-  Create summary statistics and visualizations (Ruilin)
-  Build our own variables in the merged dataset. (goal contribution per 90 minutes and salary per goal contribution) (Gil)
#### Week 4
-  Perform correlation and regression analysis (Ruilin)
-  Interpret and explain our conclusion/ findings (Ruilin & Gil)
-  Submit final project materials (Ruilin & Gil)

## Ethical Data Handling and Legality / Rights
Both datasets are publicly accessible and will be used only for educational purposes in this academic project. The FBref dataset is drawn from a public MLS statistics page hosted by FBref, a public football statistics site. The MLSPA dataset is published directly by the MLS Players Association through its salary guide and is intended to provide public transparency regarding player compensation.

We will not use either dataset for commercial redistribution or resale. Instead, the data will only be used for analysis, visualization, and discussion within the course project.

To handle the data ethically we will:
- cite the original source links in the repository and report
- avoid misrepresenting the meaning of salary fields
- document any cleaning or transformation steps
- store only the data necessary for the project analysis

## Constraints
Potential constraints include:
- player and club names may not match exactly across the two sources
- salary data and performance data may reflect slightly different reporting conventions
- some players may have limited minutes which can distort totals
- some important variables such as injuries or tactical role are not included

## Gap 
There are several gaps in the planned analysis:
- salary does not capture all contract context such as incentives not included in guaranteed compensation
- performance may depend heavily on position but raw totals like goals and assists do not fully reflect defensive roles
- the project uses publicly available season statistics rather than detailed event level tracking data
Future work could incorporate position specific metrics metrics, more advanced performance indicators, or team level contextual variables.
