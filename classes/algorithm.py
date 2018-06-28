from sklearn.cluster import KMeans
from math import sqrt, pow

class algorithm:

    kmeans = []
    players_algorithm = []
    players_info = []
    players_after_cluster = []
    distance = []
    labels = []
    players_info_after_cluster = []

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
        for index in range(len(self.players_algorithm)) :
            if(self.labels[index] == cluster):
                self.players_after_cluster.append(self.players_algorithm[index])
                self.players_info_after_cluster.append(self.players_info[index])

    def reset_algorithm(self):
        self.distance = []
        self.labels = []
        self.players_algorithm = self.players_after_cluster
        self.players_info = self.players_info_after_cluster
        self.players_after_cluster = []
        self.players_info_after_cluster = []