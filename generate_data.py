import pandas as pd
import random

# Constants to make data look real
TEAMS = ['India', 'Australia', 'England', 'Pakistan', 'South Africa', 'New Zealand', 'Sri Lanka', 'West Indies']
VENUES = ['Lord\'s, London', 'MCG, Melbourne', 'Wankhede, Mumbai', 'Eden Gardens, Kolkata', 'Old Trafford, Manchester', 'Chinnaswamy, Bangalore']
PLAYERS = {
    'India': ['Virat Kohli', 'Sachin Tendulkar', 'Rohit Sharma', 'MS Dhoni', 'Yuvraj Singh'],
    'Australia': ['Ricky Ponting', 'Glenn Maxwell', 'Steve Smith', 'David Warner', 'Adam Gilchrist'],
    'England': ['Joe Root', 'Ben Stokes', 'Jos Buttler', 'Eoin Morgan', 'Kevin Pietersen'],
    'Pakistan': ['Babar Azam', 'Wasim Akram', 'Inzamam-ul-Haq', 'Shahid Afridi', 'Imran Khan'],
    'South Africa': ['AB de Villiers', 'Jacques Kallis', 'Hashim Amla', 'Dale Steyn', 'Graeme Smith'],
    'New Zealand': ['Kane Williamson', 'Brendon McCullum', 'Ross Taylor', 'Martin Guptill', 'Daniel Vettori'],
    'Sri Lanka': ['Kumar Sangakkara', 'Mahela Jayawardene', 'Sanath Jayasuriya', 'Muttiah Muralitharan', 'Lasith Malinga'],
    'West Indies': ['Chris Gayle', 'Brian Lara', 'Viv Richards', 'Clive Lloyd', 'Andre Russell']
}

data = []

# Generate match data for World Cups from 1975 to 2023
for year in range(1975, 2027, 4):
    for team, players in PLAYERS.items():
        # Each major player plays ~5-8 matches per world cup
        for player in players:
            matches_played = random.randint(3, 9)
            
            for _ in range(matches_played):
                runs = random.randint(0, 150)
                is_wide = random.randint(0, 5) # Random wide balls bowled/faced
                is_no_ball = random.randint(0, 3) # Random no balls
                venue = random.choice(VENUES)
                
                # Logic for "Highest Runs in Single Innings"
                # We treat 'runs' as the score for that match
                
                record = {
                    "Year": year,
                    "Team": team,
                    "Player": player,
                    "Runs": runs,
                    "Wides": is_wide,
                    "No_Balls": is_no_ball,
                    "Venue": venue,
                    "Match_Date": f"{year}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
                }
                data.append(record)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_filename = "cricket_world_cup_data.csv"
df.to_csv(csv_filename, index=False)

print(f"✅ Data successfully generated: {csv_filename}")
print(f"   Total Records: {len(df)}")
print("   Columns: Year, Team, Player, Runs, Wides, No_Balls, Venue, Match_Date")