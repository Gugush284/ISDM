import networkx as nx
import matplotlib.pyplot as plt

class Gcore():
    def __init__(self):
        self.graph = nx.DiGraph(directed=True)
        self.edges_label = None

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

    def add_nodes_from_connections(self, connections):
        nodes = [elem[1] for elem in connections]   
        nodes.append(connections[0][0])

        self.add_nodes(nodes)

    def add_node(self, elem):
        self.graph.add_node(elem)

    def add_edges(self, edges):
        self.graph.add_edges_from(edges)

    def add_edges_with_label(self, connections):
        self.add_edges([(elem[0], elem[1]) for elem in connections])

        self.edges_label = dict([((elem[0], elem[1]), elem[2]) for elem in connections])

    def show(self):
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx(self.graph, pos, **(self.options))

        if self.edges_label is not None:
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=self.edges_label)

        plt.show()

if __name__ == "__main__":
    g = Gcore()

    g.info()

    g.add_nodes(['1', '2'])

    g.info()

    g.show()