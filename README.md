# Major League Soccer Performance and Salary Analysis
## Contributors

* Gil Montiel
* Ruilin Fan

## Summary
The objective of this project is to explore the correlation between player performance and salary within Major League Soccer (MLS). Based on fundamental logic, it is a natural assumption that the more exceptional a player's performance, the higher their earnings should be. This notion is a common theme in discussions across various sports disciplines. However, when we examine actual empirical data, the reality is often far more complex. Salary determinations are rarely predicated solely on a player's on-field performance; factors such as seniority, reputation, and even the timing of contract signings can all play a significant role. Consequently, we aim to conduct an in-depth investigation to precisely quantify the extent to which "performance" actually dictates salary levels.

The central question guiding our team's research is this: How exactly does player performance influence salary levels within the MLS? In the process of sorting out and analyzing the data, another question naturally arises: Are there any players whose salaries are significantly different from their actual performance and deserve (i.e., too high or too low)? If such discrepancies indeed exist, they would serve as a fascinating point of entry, revealing specific instances where a player's actual on-field performance does not fully align with the remuneration they receive.

To investigate this issue, our team utilized two distinct datasets. One set of statistics includes all players' data for the 2025 MLS season, specifically covering indicators such as goals, assists, and appearances. These indicators are generally considered key metrics for measuring a player's performance. The second dataset originates from the MLS Players Association and focuses specifically on player compensation; this dataset provides a detailed breakdown of each player's base salary as well as their total guaranteed compensation. These two datasets capture different dimensions of the same subject from distinct perspectives; only by integrating them can we establish a solid foundation for our subsequent analysis.

Upon commencing the data processing phase, we quickly identified several issues requiring immediate attention. Foremost among these was the lack of consistency in the formatting of player names across the two datasets: some names contained extraneous spaces, while others exhibited discrepancies in capitalization. Secondly, salary data cannot be used directly because these values are stored in the original data in a "text" format that includes currency symbols, rather than a standard "numerical" format. These various issues clearly demonstrated that, before undertaking any substantive analysis, the raw data first required thorough cleaning and preprocessing.

Although the data cleaning process itself is not complex, it constitutes an indispensable and critical stage. We began by standardizing player names to ensure precise matching between the two datasets; subsequently, we uniformly converted the salary data from text format to numeric format. Additionally, we removed duplicate rows from the dataset and filtered out entries containing incomplete information. Following this series of cleaning and preprocessing steps, the two datasets were successfully merged using "Player Name" as the common key field.

Based on the merged dataset, we proceeded to analyze the dynamic relationship between player salaries and their on-field performance. we generated scatter plots visualizing the relationship between salary levels and metrics such as goals scored and assists provided, and calculated the correlation coefficients between them. The analysis revealed a distinct upward trend in salary levels: players with higher goal tallies or greater contributions in terms of assists tended to command relatively higher salaries. However, we also noted that this positive correlation between "performance and salary" was not exceptionally tight; a certain degree of looseness remained between the two variables. The data points were somewhat scattered, implying that players with comparable performance levels could still exhibit significant disparities in their salary levels.

The performance-to-salary profiles of certain players proved particularly noteworthy: a small minority of players commanded high salaries despite lacking impressive statistical metrics, while others, despite delivering outstanding performances, failed to reach the ranks of top earners. This suggests that on-field performance is merely one of several factors influencing salary decisions; it is highly probable that other factors—which are not captured within this specific dataset—are also at play.

Ultimately, this project demonstrates that while on-field performance is indeed crucial, it is not the sole determinant of a player's salary. Furthermore, the project illustrates how integrating disparate datasets can enable us to address questions that cannot be resolved using a single data source alone. Throughout the research process, the data processing stage, especially the data cleaning and matching, proved to be just as important as the final data analysis stage.

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
