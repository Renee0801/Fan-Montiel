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

This project uses two datasets that describe MLS players from different perspectives. One focuses on performance during the 2025 season, while the other focuses on salary. Each dataset is stored separately in the project repository and is used at different stages of the workflow.

### Dataset 1: FBref 2025 Major League Soccer Player Statistics

The first dataset contains player performance statistics for the 2025 MLS season. The file is in Excel format, and each row represents one player. The columns include variables such as player name, team, goals, assists, and appearances. These variables describe how players perform during matches. The dataset is relatively structured, with clear column headers, but there are still small inconsistencies. For example, player names are not always formatted in the same way, and some fields may contain missing values. These issues do not prevent use, but they require attention before analysis.

Expected repository location: `data/raw/MLS_Salary_2025_Fall_Release_Original.csv`

Processed repository location:


The relevant fields include player name, squad or club, position, age, matches played, starts, minutes, goals, and assists. These variables are stored in a tabular structure and are appropriate for Pandas processing. The performance dataset answers the project questions by providing measurable indicators of player output. Goals and assists are especially important for attacking production, while minutes played helps adjust comparisons between regular starters and low minute players.

The raw FBref table contains some formatting issues that need to be handled before analysis. In the original notebook, the first row had to be treated as the column header, duplicate column names had to be removed, and numeric fields such as minutes, goals, and assists had to be converted from text into numeric values. Some rows also repeated header content or did not represent valid player observations. The cleaning script removes invalid rows and keeps the relevant columns needed for integration and analysis.

The main limitation of the FBref dataset is that raw goals and assists do not fully represent every position. Defenders, goalkeepers, and defensive midfielders may have strong value without producing high attacking totals. For this reason, our findings are most directly meaningful for attacking and creative players. The dataset is public, but it is still important to cite FBref and avoid implying ownership of the original data.

### Dataset 2: MLS Players Association Salary Guide

The second dataset contains salary information from the MLS Players Association. This dataset is in CSV format, and each row also represents a player. The main variables include player name, base salary, and guaranteed compensation. Compared to the performance dataset, this one is more focused and contains fewer variables. One characteristic of this dataset is that salary values are stored as text with currency symbols and commas. This means the values cannot be used directly for numerical analysis and must be converted into numeric format.

Raw repository location: `data/raw/MLS_Salary_2025_Fall_Release.csv`

Processed repository location: `data/processed/salary_cleaned.csv`

The relevant fields include first name, last name, team name, position, base salary, and guaranteed compensation. The raw file stores salary values with dollar signs and commas, so those fields must be cleaned before analysis. The raw file also separates first and last names, while the FBref dataset uses one player name field. To create a compatible merge key, we combined first and last names into a full player name.

The salary dataset contributes the financial side of the project. It allows us to test whether players with higher guaranteed compensation also have higher statistical output. It also supports efficiency measures such as salary per goal contribution.

There are some legal and ethical constraints. The dataset is public and published by the MLS Players Association for transparency, but our project uses it only for educational analysis. We do not redistribute the data commercially or make claims about a player's worth beyond the limited statistics available. Salary is personally identifiable professional compensation information, so the report avoids judgmental language and frames results as analytical comparisons based on public data.

### Relationship Between the Datasets

NEED TO COMPLETE!!!!!!!


## Data Quality

Before merging the datasets, we conducted a thorough quality check and carefully reviewed the data sources. Understanding the origin of the data is crucial, as it helps to clarify both its strengths and its inherent limitations—a principle we learned during our coursework.

The first dataset was scraped from the FBref website and contains player statistics for the 2025 MLS (Major League Soccer) season. FBref is a widely recognized and specialized public resource for football statistics, with its dedicated MLS section providing comprehensive player-level data. This dataset encompasses variables such as player names, clubs, positions, ages, appearances, minutes played, goals scored, and assists. Some tables within the dataset also provide advanced statistical metrics, such as "Expected Goals" (xG) and "Expected Assists" (xA). Given that this data originates from a reputable platform and adheres to a standardized structure, its overall reliability is high. However, upon closer inspection, we did identify some minor issues: player name formatting was not always entirely consistent, and some fields contained missing values. Although such issues are not uncommon in data processing, they nonetheless require careful handling.

The second dataset was sourced from the salary guide published by the MLS Players Association. This dataset compiles salary information for all active, signed players as of October 1, 2025. It includes two key metrics: "Base Salary" and "Guaranteed Compensation." According to the source's documentation, "Guaranteed Compensation" comprises the base salary plus any guaranteed bonuses, but excludes performance-based bonuses contingent upon individual achievement. The dataset features variables such as players' first names, last names, clubs, positions, and specific salary figures. Given that this data is publicly released by an official organization, its credibility is exceptionally high. Nevertheless—much like the aforementioned player performance dataset—this salary dataset also presents formatting challenges: the salary figures are stored as text strings containing currency symbols and comma separators, rendering the data unsuitable for direct use in subsequent statistical analysis.

Following a comprehensive review of the two datasets described above, a number of data quality issues emerged. The most prominent issue among these is the inconsistency in player names. The two datasets exhibit subtle differences in name formatting; even minor discrepancies can prevent the data from being correctly matched and linked. Given that this data integration project is structured around the "player" as the fundamental unit, this issue of name inconsistency will directly impact the success rate of the data merging operations.

Furthermore, both datasets contain missing values. In the player performance dataset, statistical data for certain players is incomplete—a phenomenon likely attributable to their limited playing time. Similarly, within the salary dataset, a small number of entries suffer from incomplete or entirely missing data. Failure to properly address these data gaps could introduce bias into subsequent analytical results; this impact is particularly pronounced when investigating the interrelationships between various variables.

Additionally, we observed the presence of duplicate records. Records for certain players appear multiple times, which could lead to double-counting. If these duplicates are not removed, the results may be skewed, thereby compromising the accuracy of aggregate statistics.

Another issue concerns data types. Salary figures are stored as strings rather than numerical values. Consequently, they cannot be directly utilized in computational tasks such as correlation analysis or data visualization. Without proper type conversion, the dataset cannot support quantitative analysis.

Although the overall structure of these datasets is sound and their sources are reliable, they are not yet in a state ready for immediate analysis. Most of the identified issues relate to data consistency, formatting standards, and completeness. Such problems are quite common when handling real-world data derived from multiple sources.

In summary, while the overall quality of the dataset is fair, it still requires data cleaning before it can be put to use. By proactively identifying and resolving these issues, we can properly prepare the data for integration, thereby ensuring that subsequent analytical work is built upon a foundation of consistent and reliable information.

## Data Cleaning

After identifying several issues within the two datasets, we executed a series of data cleaning steps aimed at rendering the data suitable for integration and analysis. The objective of this process was not to alter the original content of the data itself, but rather to ensure sufficient consistency and reliability to support meaningful comparative analysis.

First, we standardized the player names. Since the two datasets employed slightly different formats, a direct, exact match was not initially possible. To resolve this issue, we converted all player names to lowercase and removed any leading or trailing whitespace. Although seemingly minor, this step had a significantly positive impact on the number of successfully matched records during the data integration process; without this adjustment, many records would not have aligned correctly.

Another critical step focused on salary data. In its raw state, salary figures were stored in a text format that included non-numeric characters, such as dollar signs and commas. While this format facilitates data presentation, it hinders the execution of numerical operations. To address this, we removed all non-numeric characters and converted the salary figures into a standardized numeric format. This process enables us to successfully perform computational tasks such as correlation analysis and generate corresponding data visualization charts.

Naturally, handling duplicate records was also an essential component of this process. During the data inspection phase, we discovered that records for certain players appeared more than once within the datasets. Retaining these duplicates would have resulted in specific players being assigned disproportionately high weight in the analysis, potentially skewing the final results. To prevent this, we identified and removed all duplicate rows, ensuring that in the cleaned dataset, each player's record appeared only once.

Handling missing values ​​also required careful attention. In the player performance dataset, statistical data for some players was incomplete; similarly, in the salary dataset, a small number of records were missing salary figures. Instead of attempting to estimate or impute missing values, we chose to directly exclude incomplete records containing missing values when they were crucial to the analysis results. This approach helps avoid introducing additional artificial assumptions or distortions into the data.

A further step involved a comprehensive review of the data types for all variables. We discovered that the data format of some columns that should have contained numerical values was not consistent. Consequently, we reviewed these columns one by one and converted them to their corresponding data types to ensure that subsequent computational tasks could be executed with complete accuracy.

Upon completing the data cleaning for both datasets individually, the next task was to prepare for data integration. Since these two datasets are linked via the "player name" field, the consistency of this specific field was of paramount importance. The series of data cleaning steps executed previously laid the foundation for achieving a more precise data merge. We used an "inner join" approach to merge the data, which means we only kept the player records that appeared in both datasets. This strategy ensured that the final dataset generated contained, for every single record, both the player's performance statistics and their salary information. Once the datasets were merged, we conducted a final verification to confirm data consistency. This verification included checking for any unexpected missing values ​​and ensuring that the data types for all columns were accurate. Subsequently, the cleaned and merged dataset was saved to the `data/processed/` directory, while the original files were retained in the `data/raw/` directory. Retaining both versions helps enhance the transparency of the data processing pipeline and facilitates the reproducibility of the workflow.

Overall, the primary focus of this data cleaning effort was to enhance data consistency, eliminate errors, and prepare the data for subsequent analysis. Although the steps taken were relatively simple and straightforward, they were crucial for ensuring the reliability of the analytical results. Had these necessary adjustments not been made, the data integration process would not have proceeded smoothly, potentially leading to analytical conclusions that were misleading.

## Findings
