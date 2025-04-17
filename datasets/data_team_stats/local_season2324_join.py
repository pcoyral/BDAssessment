#Locally joining the data for team stats season 2023-2024 from different csv files 
#I didn't find one source that had all the team data merged for the 2023-2024 season, so I had to merge the data from different leagues

import os
import pandas as pd

base_dir = "/Users/nicolasloescher-montal/Desktop/IE/YEAR 3/S2/Big Data /Code Repository/"

csv_files = {
    "Bundesliga": os.path.join(base_dir, "Bundesliga23.csv"),
    "LaLiga": os.path.join(base_dir, "LaLiga23.csv"),
    "Ligue1": os.path.join(base_dir, "Ligue1.csv"),
    "PremierLeague": os.path.join(base_dir, "PL23.csv"),
    "SerieA": os.path.join(base_dir, "SerieA23.csv"),
}

df_list = [pd.read_csv(file, encoding="utf-8").assign(League=league) for league, file in csv_files.items()]
merged_df = pd.concat(df_list, ignore_index=True)
output_file = os.path.join(base_dir, "2023-2024_Football_Team_Stats.csv")
merged_df.to_csv(output_file, index=False, encoding="utf-8")

print(f"Merged dataset saved as: {output_file}")


