MLB World Series Winning Chances Predictor
This project uses team batting and pitching statistics from current playoff-contending teams and compares them against the metrics of past MLB World Series champions (2013-2023, excluding 2020) to estimate each team's chances of winning the World Series.

Project Overview
The script analyzes team performance using the following statistics:

Batting Metrics: Runs (R), Batting Average (BA), On-Base Percentage (OBP), Slugging Percentage (SLG)
Pitching Metrics: Earned Run Average (ERA)
The past champions' statistics are stored in CSV files for both batting and pitching. The script calculates the team totals for the playoff-contending teams using current-season statistics, compares these to the historical data, and then estimates each team's winning chances based on their statistical similarity to past champions.

Key Features
Data-Driven Prediction: Uses key batting and pitching metrics to compare current teams against past World Series champions.
Team Totals: Metrics are calculated using team totals from the second-to-last row in each CSV file for accuracy.
Normalized Winning Chances: The team's winning chances are normalized so the total for all teams adds up to 100%.

File Naming Convention
Ensure that your CSV files follow the naming convention:

For each year of champion stats: YearBatting.csv and YearPitching.csv
For each team: TeamNameBatting.csv and TeamNamePitching.csv
The playoff teams' file names should include the team's name followed by either "Batting" or "Pitching", e.g., OriolesBatting.csv, OriolesPitching.csv.

All data from Baseball-Reference.com
