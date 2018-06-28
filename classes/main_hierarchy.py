from algorithm import algorithm
from process import process

player_position = 'prefers_cam'
player_id = 211110
cluster = 1

my_process = process(player_id, player_position)
my_process.process_data()

my_algorithm_hierarchy = algorithm(my_process.players_algorithm, my_process.players, 5, 300)


print('\n\nhierarchy')

for index in range(3):

    my_algorithm_hierarchy.fit()
    my_algorithm_hierarchy.set_distance()
    my_algorithm_hierarchy.set_labels()

    for index in range(len(my_algorithm_hierarchy.players_info)):
        if (my_algorithm_hierarchy.players_info[index][0] == player_id):
            cluster = my_algorithm_hierarchy.labels[index]

    my_algorithm_hierarchy.set_players_after_cluster(cluster)
    my_algorithm_hierarchy.reset_algorithm()

for player in my_algorithm_hierarchy.players_info:
    overall = 0
    for player_full in my_process.players:
        if(player[0] == player_full[0]):
            overall = player_full[2]
    print(player[1], overall)

