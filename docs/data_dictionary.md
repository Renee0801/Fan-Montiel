# Data Dictionary

## salary_cleaned.csv

| Column | Meaning |
| --- | --- |
| player_name | Player full name from the MLSPA Salary Guide |
| team_name | MLS club listed in the salary guide |
| position_clean | Player position from the salary guide |
| base_salary | Current annualized base salary in US dollars |
| guaranteed_comp | Annualized average guaranteed compensation in US dollars |
| player_key_merge | Normalized player name used for merging |
| team_key | Normalized team name used for merging |

## stats_cleaned.csv

| Column | Meaning |
| --- | --- |
| player_name | Player name from FBref |
| team_name | MLS club from FBref |
| position_clean | FBref position code |
| age | Player age |
| matches_played | Matches played |
| starts | Matches started |
| minutes | Regular season minutes played |
| goals | Goals scored |
| assists | Assists recorded |
| player_key_merge | Normalized player name used for merging |
| team_key | Normalized team name used for merging |

## mls_salary_performance_merged.csv

| Column | Meaning |
| --- | --- |
| goal_contributions | Goals plus assists |
| goals_per_90 | Goals adjusted to a 90 minute basis |
| assists_per_90 | Assists adjusted to a 90 minute basis |
| goal_contributions_per_90 | Goals plus assists adjusted to a 90 minute basis |
| salary_per_goal_contribution | Guaranteed compensation divided by goal contributions |
