from sklearn.cluster import KMeans
from math import sqrt, pow

class algorithm:

    kmeans = []
    players_algorithm = []
    players_info = []
    players_after_cluster = []
    distance_after_cluster = []
    distance = []
    labels = []

    def __init__(self, players_algorithm, players_info, number_cluster, max_iter):
        self.players_algorithm = players_algorithm
        self.players_info = players_info
        self.kmeans = KMeans(n_clusters = number_cluster, init = 'random', max_iter = max_iter)

    def fit(self):
        self.kmeans.fit(self.players_algorithm)

    def set_distance(self):
        self.distance = self.kmeans.fit_transform(self.players_algorithm)

    def set_labels(self):
        self.labels = self.kmeans.labels_

    def set_players_after_cluster(self, cluster):
        for index, player_auxiliary in self.players_algorithm:
            if(self.labels[index] == cluster):
                self.players_after_cluster.append([player_auxiliary], self.players_info[index][0], self.players_info[index][1])

    def set_distance_after_cluster(self, player):
        for player_auxiliary in self.players_after_cluster:
            d0 = player_auxiliary[0] - player[0]
            d1 = player_auxiliary[1] - player[1]
            d2 = player_auxiliary[2] - player[2]
            d3 = player_auxiliary[3] - player[3]
            d4 = player_auxiliary[4] - player[4]
            d5 = player_auxiliary[5] - player[5]
            distance_auxiliary = sqrt(pow(d0, 2) + pow(d1, 2) + pow(d2, 2) + pow(d3, 2) + pow(d4, 2) + pow(d5, 2))
            self.distance_after_cluster.append(distance_auxiliary)
        
        self.distance_after_cluster.sort()
