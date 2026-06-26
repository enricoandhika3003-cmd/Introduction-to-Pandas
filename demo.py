import pandas as pd

#PART 1
print('--- PART 1: Pandas Series ---')
scores = [98500,87200, 76400, 65100, 54800, 67420]
players = pd.Series(scores, index=['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm', 'mastergamer7742'])
print(players)

#PART 2
print("\n")
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Player': ['NightWolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm', 'mastergamer7742'],
    'Level': [42, 38, 35, 30, 27, 67],
    'HighScore': [98500, 87200, 76400, 65100, 54800, 67420],
    'Wins': [210, 185, 162, 140, 118, 420]
}
df = pd.DataFrame(data)
print(df)

#PART 3
print("\n")
print('--- PART 3: Accessing Rows ---')
print('Row 0 (top player): ')
print(df.loc[0])
print("\n")
print('Rows 2 and 3: ')
print(df.loc[2:3])

#PART 4
print("\n")
print('--- PART 4: Reading a CSV File ---')
full_df = pd.read_csv('leaderboard.csv')
print('First 5 rows (head): ')
print(full_df.head())
print("\n")
print('Last 3 rows (tail): ')
print(full_df.tail(3))
print("\n")
print('Dataset info: ')
print(full_df.info())

#PART 5
print("\n")
print('--- PART 5: Cleaning Data ---')
print('Rows with missing values removed (dropna): ')
clean_df = full_df.dropna()
print(clean_df.to_string())
print("\n")
print('Missing values filled with 0 (fillna): ')



