import pandas as pd

class process:

    players_algorithm = []
    players = []
    player_id = []
    preference_position = ''
    
    def __init__(self, player_id, preference_position):
        self.player_id = player_id
        self.preference_position = preference_position

    def process_data(self):
        players_database = pd.read_csv('../csvs/complete.csv')
        for index, player in players_database.iterrows():
            if(player[self.preference_position] and index < 4000):
                player_transformed = [player['pac'], player['sho'], player['pas'], player['dri'], player['def'], player['phy']]
                self.players_algorithm.append(player_transformed)
                self.players.append([player['ID'], player['name'], player['overall']] + player_transformed)
