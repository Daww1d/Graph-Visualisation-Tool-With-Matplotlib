import matplotlib.pyplot as plt
import networkx as nx

adjecency = [[0,3,1,1], #example matrix
             [3,0,1,0],
             [1,1,0,1],
             [1,0,1,1]]

class Graph():

    def __init__(self, matrix, edgeColour='black', vertexColour='blue'):
        self.matrix = matrix # Matrix of the graph object
        self.vertexNum = len(self.matrix) # Number of verticies in the matrix
        self.vertexes = [i + 1 for i in range(self.vertexNum)] # Creates a list for all verticies in list and numbers them and added 1 to index from 1 not 0
        self.edgeColour = edgeColour
        self.vertexColour = vertexColour

    def drawGraph(self):

        #Creates instance of graph in library
        graph = nx.MultiGraph()

        #Adds vertexes to graph
        graph.add_nodes_from(self.vertexes) #Adds vertexes to graph

        #Adds edges to graph
        for i in range(self.vertexNum):
            for j in range(i, self.vertexNum):
                if self.matrix[i][j] != 0:
                    for k in range(self.matrix[i][j]):#adds edge multiple times based on value
                        if self.matrix[i][j] % 2 == 0:
                            graph.add_edge(i+1, j+1 , curviture= (0.1 * ((-1) ** k) * (((k+1)//2) * 0.5)))
                        elif self.matrix[i][j] % 2 != 0:
                            if k == 0: #Creates straight connection if only one connection
                                graph.add_edge(i+1, j+1 , curviture=0)
                            else:
                                graph.add_edge(i+1, j+1 , curviture= (0.1 * ((-1) ** k) * (((k+1)//2) * 0.5)))
        
        #Draw graph
        layout = nx.spring_layout(graph, seed=0) #Uses the inbuilt spring layout to remove overlaps, seed being constant produces replicatable results

        #Draw each node
        nx.draw_networkx_nodes(graph, layout, node_color=self.vertexColour)
           
        #Draw each edge
        for u, v, data in graph.edges(data=True):
            rad = data['curviture'] #Extract radius from vertexes
            nx.draw_networkx_edges(graph, layout, [(u,v)], connectionstyle=f'arc3,rad={rad}', edge_color=self.edgeColour)

        #Create window that displays graph
        plt.show()


G = Graph(adjecency)
G.drawGraph()