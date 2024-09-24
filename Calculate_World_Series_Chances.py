import os
import pandas as pd

# Define playoff teams and their file names
playoff_teams = ["Orioles", "Yankees", "Guardians", "Astros", "Royals", "Tigers", "Twins", 
                 "Mariners", "Dodgers", "Phillies", "Brewers", "Padres", "Mets", 
                 "Diamondbacks", "Braves"]

# Load champion metrics from 2013 to 2023 (excluding 2020)
champion_years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2021, 2022, 2023]
champion_metrics = []

for year in champion_years:
    batting_file = f"{year}Batting.csv"
    pitching_file = f"{year}Pitching.csv"
    
    if os.path.exists(batting_file) and os.path.exists(pitching_file):
        batting_data = pd.read_csv(batting_file)
        pitching_data = pd.read_csv(pitching_file)
        
        # Use the second-to-last row for team totals
        champion_batting_metrics = batting_data.iloc[-2]  # Assuming team totals is the second-to-last row
        champion_pitching_metrics = pitching_data.iloc[-2]

        # Store relevant team stats
        champion_batting = {
            'R': champion_batting_metrics['R'],
            'BA': champion_batting_metrics['BA'],
            'OBP': champion_batting_metrics['OBP'],
            'SLG': champion_batting_metrics['SLG']
        }
        
        champion_pitching = {
            'ERA': champion_pitching_metrics['ERA']
        }

        # Combine batting and pitching stats into one
        champion_metrics.append({**champion_batting, **champion_pitching})

# Convert list of dicts to DataFrame for easier processing
champion_metrics_df = pd.DataFrame(champion_metrics)

# Initialize a dictionary to store winning chances for each team
winning_chances = {}

# Analyze each playoff team's 2024 stats
for team in playoff_teams:
    batting_file = f"{team}Batting.csv"
    pitching_file = f"{team}Pitching.csv"

    print(f"Processing {team}...")

    if os.path.exists(batting_file):
        batting_data = pd.read_csv(batting_file)
        
        # Use team totals row (second-to-last row)
        team_batting_metrics = batting_data.iloc[-2]
        batting_metrics = {
            'R': team_batting_metrics['R'],
            'BA': team_batting_metrics['BA'],
            'OBP': team_batting_metrics['OBP'],
            'SLG': team_batting_metrics['SLG']
        }

        print(f"{team} Batting Metrics: {batting_metrics}")

        pitching_metrics = {'ERA': 0}
        if os.path.exists(pitching_file):
            pitching_data = pd.read_csv(pitching_file)
            team_pitching_metrics = pitching_data.iloc[-2]
            pitching_metrics['ERA'] = team_pitching_metrics['ERA']
            print(f"{team} Pitching Metrics: {pitching_metrics}")
        else:
            print(f"{team} pitching file not found: {pitching_file}")

        # Compare against champion metrics
        total_score = 0
        for index, champion in champion_metrics_df.iterrows():
            score = 0
            score += (batting_metrics['R'] / champion['R']) if champion['R'] > 0 else 0
            score += (batting_metrics['BA'] / champion['BA']) if champion['BA'] > 0 else 0
            score += (batting_metrics['OBP'] / champion['OBP']) if champion['OBP'] > 0 else 0
            score += (batting_metrics['SLG'] / champion['SLG']) if champion['SLG'] > 0 else 0
            score += (pitching_metrics['ERA'] / champion['ERA']) if champion['ERA'] > 0 else 0
            
            total_score += score

        # Calculate average score as the team's winning chance percentage
        winning_chances[team] = total_score / len(champion_metrics_df)
        print(f"{team} Winning Chance Percentage: {winning_chances[team]}")

    else:
        print(f"{team} batting file not found: {batting_file}")

# Normalize the winning chances so they sum to 100%
total_score = sum(winning_chances.values())
normalized_winning_chances = {team: (score / total_score) * 100 for team, score in winning_chances.items()}

# Sort teams by their normalized winning chances (from highest to lowest)
sorted_winning_chances = sorted(normalized_winning_chances.items(), key=lambda x: x[1], reverse=True)

# Print sorted normalized percentages
print("\nNormalized Winning Chance Percentages (Highest to Lowest):")
for team, percentage in sorted_winning_chances:
    print(f"{team}: {percentage:.2f}%")