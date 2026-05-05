# Major League Soccer Performance and Salary Analysis
## Contributors

* Gil Montiel
* Ruilin Fan

## Summary

This project examines whether Major League Soccer player compensation reflects measurable on field performance during the 2025 season. MLS clubs make major financial decisions when signing, extending, and retaining players, but salary is not always directly connected to statistical output. A high salary may reflect past performance, marketability, scarcity at a position, leadership, contract timing, or international reputation. At the same time, clubs and analysts still need a structured way to evaluate whether payroll spending is connected to actual player production. Our project approaches this issue as a data curation and integration problem rather than only as a sports question.

The main research question is: do higher paid MLS players produce stronger on field performance statistics? We also ask which performance measures are most associated with salary, whether some players appear underpaid or overpaid relative to production, and how efficiently teams convert player salary spending into measurable attacking output. To answer these questions, we integrated two public data sources. The first source is the 2025 MLS player statistics table from FBref, which contains player level performance information such as club, position, minutes played, goals, assists, and starts. The second source is the 2025 MLS Players Association Salary Guide, which contains player compensation information including annualized base salary and annualized average guaranteed compensation.

The project follows a data lifecycle model that moves from data acquisition, storage, cleaning, integration, analysis, documentation, and reproducibility. The two datasets were first stored as raw files, then cleaned into standardized processed files. Because the two sources use different naming conventions, a major part of the project involved normalizing player names, club names, and salary fields. We created merge keys for player and club names, removed non player salary records, converted salary values into numeric values, and removed invalid statistics rows. After cleaning, the datasets were integrated at the player and club level using Python and Pandas.

Our current integrated dataset links the salary and performance records for most players who appear in both sources. The status report stage showed that the cleaned statistics data had 882 player observations, the cleaned salary data had 931 salary records after removing non player entries, and the cleaned name and club merge produced 664 matched player records. This match rate is strong enough for exploratory analysis, while still showing the real world difficulty of integrating public sports datasets from separate providers.

The analysis focuses on salary distributions, goal contributions, goals per 90 minutes, and salary per goal contribution. These derived variables help compare players with different playing time levels. A central lesson from the project is that salary and performance can be compared, but they should not be interpreted too simplistically. Salary is a financial and contractual variable, while performance statistics depend on playing time, position, team role, injuries, and tactical context. For that reason, the project emphasizes transparent data handling and careful documentation of limitations.

## Data Profile

### Dataset 1: FBref 2025 Major League Soccer Player Statistics

The first dataset is the 2025 MLS player statistics table from FBref. FBref is a public football statistics website that provides season level player and team statistics. The project uses the standard player statistics table for Major League Soccer. This table is useful because it gives performance information at the player level and includes variables that can be linked to salary data.

Expected repository location: `data/raw/MLS_Salary_2025_Fall_Release_Original.csv`

Processed repository location:


The relevant fields include player name, squad or club, position, age, matches played, starts, minutes, goals, and assists. These variables are stored in a tabular structure and are appropriate for Pandas processing. The performance dataset answers the project questions by providing measurable indicators of player output. Goals and assists are especially important for attacking production, while minutes played helps adjust comparisons between regular starters and low minute players.

The raw FBref table contains some formatting issues that need to be handled before analysis. In the original notebook, the first row had to be treated as the column header, duplicate column names had to be removed, and numeric fields such as minutes, goals, and assists had to be converted from text into numeric values. Some rows also repeated header content or did not represent valid player observations. The cleaning script removes invalid rows and keeps the relevant columns needed for integration and analysis.

The main limitation of the FBref dataset is that raw goals and assists do not fully represent every position. Defenders, goalkeepers, and defensive midfielders may have strong value without producing high attacking totals. For this reason, our findings are most directly meaningful for attacking and creative players. The dataset is public, but it is still important to cite FBref and avoid implying ownership of the original data.

### Dataset 2: MLS Players Association Salary Guide

The second dataset is the 2025 MLS Players Association Salary Guide. This source reports salary information for MLS players under contract as of October 1, 2025. It includes current annualized base salary and annualized average guaranteed compensation. Guaranteed compensation includes base salary plus signing and guaranteed bonuses annualized over the contract term, but it does not include performance bonuses.

Raw repository location: `data/raw/MLS_Salary_2025_Fall_Release.csv`

Processed repository location: `data/processed/salary_cleaned.csv`

The relevant fields include first name, last name, team name, position, base salary, and guaranteed compensation. The raw file stores salary values with dollar signs and commas, so those fields must be cleaned before analysis. The raw file also separates first and last names, while the FBref dataset uses one player name field. To create a compatible merge key, we combined first and last names into a full player name.

The salary dataset contributes the financial side of the project. It allows us to test whether players with higher guaranteed compensation also have higher statistical output. It also supports efficiency measures such as salary per goal contribution.

There are some legal and ethical constraints. The dataset is public and published by the MLS Players Association for transparency, but our project uses it only for educational analysis. We do not redistribute the data commercially or make claims about a player's worth beyond the limited statistics available. Salary is personally identifiable professional compensation information, so the report avoids judgmental language and frames results as analytical comparisons based on public data.

### Relationship Between the Datasets

The two datasets are complementary because one measures compensation and the other measures performance. They can be linked by player name and club name. However, direct matching is not always simple because club names and player names may differ across sources. Examples include shortened team names, accent marks, suffixes such as Jr., and different naming conventions for transferred players. We therefore created standardized player and team merge keys.

The integration strategy uses a player key and team key. The player key removes accents, punctuation, suffixes, capitalization differences, and extra spacing. The team key applies team name mappings and then performs the same normalization. The final merged file is stored at: .......


## Data Quality

The project identified several data quality issues across the two sources. The first issue was schema inconsistency. FBref stores player names in one column named Player, while the salary guide stores names in separate First Name and Last Name columns. FBref uses Squad for club, while the salary guide uses Team Name. These structural differences required column renaming and field construction before the datasets could be compared.

The second issue was syntactic inconsistency. Salary values were stored as strings with dollar signs and commas. These formatting characters prevented direct numerical analysis. The cleaning workflow converted base salary and guaranteed compensation into numeric floating point values. Similarly, statistics columns such as minutes, goals, assists, starts, and matches played were converted into numeric fields.

The third issue was semantic inconsistency in team names. The two sources used different versions of some club names. Examples from the project include Atlanta Utd versus Atlanta United, D.C. United versus DC United, NYCFC versus New York City, and Vancouver W'Caps versus Vancouver Whitecaps. Without standardization, these records would fail to merge even if they referred to the same club. The cleaning workflow uses a club mapping dictionary and normalized team keys to reduce these errors.

The fourth issue was player name variation. Names may contain accents, punctuation, suffixes, or alternate formatting. For example, suffixes such as Jr. and accent marks can make the same player appear different across datasets. The cleaning process normalizes names by converting to lowercase, removing accents, removing punctuation, removing suffixes, and trimming repeated spaces. This improves matching while preserving the original names in separate columns.

The fifth issue was duplicate or transferred player records. Some players may appear more than once in the statistics dataset if they played for multiple clubs during the season. This creates a challenge because the salary guide lists the player under one team at the time of the salary release. To avoid double counting, the workflow sorts by minutes and keeps the observation with the highest minutes played as the player's primary season record.

The sixth issue was coverage mismatch. Not every salary guide player appears in the FBref performance table, and not every FBref player appears in the salary guide. Reasons may include timing differences, roster changes, short term contracts, transfers, missing statistics, or naming differences that remain unresolved. The current workflow produced 664 matched records in the project notebook after name and club standardization. This is a good result for analysis, but unmatched records remain a limitation.

Overall, the quality assessment shows that both datasets are usable, but only after cleaning and careful integration. The most important quality risk is false non matches caused by naming differences. The project addresses this risk through explicit merge keys, club mapping, duplicate handling, and documentation of unmatched records.
