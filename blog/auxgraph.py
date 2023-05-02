import matplotlib.pyplot as plt
import networkx as nx
from time import time


def plot_graph_simple(G: nx.classes.graph.Graph, node_size=1000):
    opts = {
        "font_size": 16, "node_size": node_size, "font_color": "whitesmoke",
        "width": 1.5, "with_labels": True,
        "font_family": "sans-serif", "edge_color": "green"
    }

    fig, ax = plt.subplots(figsize=(18, 8))
    nx.draw_networkx(G, **opts)
    fig.set_facecolor('#003049')
    ax.axis('off')
    ax.margins(0.05)
    plt.show()


def plot_graph(G: nx.classes.graph.Graph, values: list, labels: dict, name:str, node_size=1000):
    opts = {
        "font_size": 16, "node_size": node_size, "font_color": "whitesmoke",
        "width": 1.5, "node_color": values, "labels": labels, "with_labels": True,
        "font_family": "sans-serif", "edge_color": "green"
    }

    fig, ax = plt.subplots(figsize=(18, 8))
    nx.draw_networkx(G, **opts)
    fig.set_facecolor('#003049')
    ax.axis('off')
    ax.margins(0.05)
    plt.show()


class Stats():
    
    def __init__(self):
        self.round_len = 5
    
    def log_time(self, msg, start_time):
        end = time()
        elapsed = end - start_time
        print('{:>40s}     {:}'.format(msg, elapsed))

    def density(self, G: nx.classes.graph.Graph):
        start_time = time()
        try:
            density = round(nx.density(G), self.round_len)
        except nx.NetworkXError as e:
            density = str(e)
        self.log_time('Density', start_time)
        return density

    def radius(self, G: nx.classes.graph.Graph):
        start_time = time()
        try:
            radius = round(nx.radius(G), self.round_len)
        except nx.NetworkXError as e:
            radius = str(e)
        self.log_time('Radius', start_time)
        return radius

    def diameter(self, G: nx.classes.graph.Graph):
        start_time = time()
        try:
            diameter = round(nx.diameter(G), self.round_len)
        except nx.NetworkXError as e:
            diameter = str(e)
        self.log_time('Diameter', start_time)
        return diameter

    def average_shortest_path(self, G: nx.classes.graph.Graph):
        start_time = time()
        try:
            average_shortest_path = round(
                nx.average_shortest_path_length(G), self.round_len)
        except nx.NetworkXError as e:
            average_shortest_path = str(e)
        self.log_time('Average shortest path length', start_time)
        return average_shortest_path

    def average_degree(self, G: nx.classes.graph.Graph):
        start_time = time()
        G_deg = nx.degree_histogram(G)
        G_deg_sum = [a * b for a, b in zip(G_deg, range(len(G_deg)))]
        average_degree = round(
            sum(G_deg_sum) / G.number_of_nodes(), self.round_len)
        self.log_time('Average Degree', start_time)
        return average_degree

    def betweenness_centrality(self, G: nx.classes.graph.Graph):
        # Run betweenness centrality
        start_time = time()
        k = int(float(G.number_of_nodes()) / 100 * float(10))
        #betweenness_dict = nx.betweenness_centrality(self.G)
        betweenness_dict = nx.betweenness_centrality(G, k=k)
        self.log_time('Betweenness centrality', start_time)
        return betweenness_dict

    def closeness_centrality(self, G: nx.classes.graph.Graph, _is: list):
        # Run closeness centrality
        start_time = time()
        closeness_dict = {g: nx.closeness_centrality(G, u=g) for g in _is}
        self.log_time('Closeness centrality', start_time)
        return closeness_dict

    def degree_centrality(self, G: nx.classes.graph.Graph):
        # Run degree centrality
        start_time = time()
        degree_dict = nx.degree_centrality(G)
        self.log_time('Degree centrality', start_time)
        return degree_dict

    def eigenvector_centrality(self, G: nx.classes.graph.Graph):
        # Run eigenvector centrality
        start_time = time()
        eigenvector_dict = nx.eigenvector_centrality(G, max_iter=1000)
        self.log_time('Eigenvector centrality', start_time)
        return eigenvector_dict

    def clustering_coefficient(self, G: nx.classes.graph.Graph):
        # Run clustering coefficient
        start_time = time()
        clustering_dict = nx.clustering(G)
        self.log_time('Clustering coefficient', start_time)
        return clustering_dict
    
    def run_stats(self, betweenness, closeness, degree, eigenvector, clustering, _is):
        return [
            {
                'node': i,
                'degree_centrality': round(degree[i], self.round_len),
                'closeness_centrality': round(closeness[i], self.round_len),
                'betweenness_centrality': round(betweenness[i], self.round_len),
                'eigenvector_centrality': round(eigenvector[i], self.round_len),
                'clustering_coefficient': round(clustering[i], self.round_len),
            }
            for i in _is
        ]


def network_statistics(G: nx.classes.graph.Graph):
    stats = Stats()

    print('Métricas iniciais da rede...')
    print(f'\n{str(G)}')
    #print(f'\n{nx.info(G)}')
    print("\n%40s    %s" % ('Process', 'Time'))
    print("%40s    %s" % ('='*40, '='*25))

    # Run density, diameter & radius network
    density = stats.density(G)
    diameter = stats.diameter(G)
    radius = stats.radius(G)
    # Run calculating average shortest path length
    average_shortest_path = stats.average_shortest_path(G)
    # Run average degree
    average_degree = stats.average_degree(G)

    try:
        is_connected = nx.is_connected(G)
    except Exception as e:  # nx.NetworkXError as e:
        is_connected = str(e)

    try:
        number_connected_components = nx.number_connected_components(G)
    except Exception as e:  # nx.NetworkXError as e:
        number_connected_components = str(e)

    return {
        'number_of_nodes': G.number_of_nodes(),
        'number_of_edges': G.number_of_edges(),
        'density': density,
        'diameter': diameter,
        'radius': radius,
        'average_shortest_path':average_shortest_path,
        'average_degree': average_degree,
        'is_connected': is_connected,
        'number_connected_components': number_connected_components,
    }
