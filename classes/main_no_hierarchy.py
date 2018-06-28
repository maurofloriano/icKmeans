from algorithm import algorithm
from process import process

player_position = 'prefers_cam'
player_id = 211110
cluster = 1

my_process = process(player_id, player_position)
my_process.process_data()

my_algorithm = algorithm(my_process.players_algorithm, my_process.players, 60, 500)

my_algorithm.fit()
my_algorithm.set_distance()
my_algorithm.set_labels()

print('\n\nno hierarchy')

for index in range(len(my_algorithm.players_info)):
    if (my_algorithm.players_info[index][0] == player_id):
       cluster = my_algorithm.labels[index]

my_algorithm.set_players_after_cluster(cluster)
my_algorithm.reset_algorithm()

for player in my_algorithm.players_info:
    overall = 0
    for player_full in my_process.players:
        if(player[0] == player_full[0]):
            overall = player_full[2]
    print(player[1], overall)