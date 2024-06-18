import networkx as nx
import matplotlib.pyplot as plt

class Gcore():
    def __init__(self):
        self.graph = nx.DiGraph(directed=True)

        self.options = {
            'node_color': 'lightblue',     # color of node
            'node_size': 5000,          # size of node
            'width': 1,                 # line width of edges
            'arrowstyle': '-|>',        # array style for directed graph
            'arrowsize': 18,            # size of arrow
            'edge_color':'black',        # edge color
        }

    def info(self):
        print(self.graph)

    def add_nodes(self, array):
        self.graph.add_nodes_from(array)

    def add_node(self, elem):
        self.graph.add_node(elem)

    def add_edges(self, edges):
        self.graph.add_edges_from(edges)

    def show(self):
        nx.draw(self.graph, with_labels = True, **(self.options))

        plt.show()

if __name__ == "__main__":
    g = Gcore()

    g.info()

    g.add_nodes(['1', '2'])

    g.info()

    g.show()