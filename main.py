import pandas as pd

PLAYER_POSITION_PREFERENCE = 'prefers_lm'


players_database = pd.read_csv('complete.csv')

players_algorithm = []
players = []

for index, player in players_database.iterrows():
    if(player[PLAYER_POSITION_PREFERENCE]):
        player_transformed = [player['pac'], player['sho'], player['pas'], player['dri'], player['def'], player['phy']]
        players_algorithm.append(player_transformed)
        players.append([player['ID'], player['name']] + player_transformed)

print(players)

