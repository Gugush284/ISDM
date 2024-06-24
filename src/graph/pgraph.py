from graph.graphCore import Gcore

class PGraph():
    def __init__(self, connections):
        self.connections = connections
        self.gr = Gcore()

    def __get_connections__(self):
        connections = self.connections

        print(connections)

        array = []

        for elem in connections:
            con = elem[3].split(', ')

            if con[0] == '':
                array.append((elem[1], elem[2], elem[4]))
            else:
                array.append((elem[1], con[0], elem[4]))

                for i in range(len(con) - 1):
                    array.append((con[i], con[i + 1], elem[4]))

                array.append((con[len(con) - 1], elem[2], elem[4]))

        return array
    
    def graph(self):

        connections = self.__get_connections__()

        self.gr.add_nodes_from_connections(connections)

        self.gr.add_edges_with_label(connections)

        #g.info()

        self.gr.show()