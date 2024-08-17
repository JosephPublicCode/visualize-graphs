import random as rn
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from dfs import DFS 
    

    
# visualize the graphs using 
class Visualize: 
    def visualize_search(self, order, positions, graph, title): 

        fig = plt.figure() 
        plt.title(title)
        for i,node in enumerate(order ,start=1): 
            plt.clf()
            plt.title(title)
            nx.draw(graph,positions,
                    with_labels=True, 
                    node_size = 1000, 
                    font_weight = 'bold', 
                    node_color=['tab:red' if n == node else 'tab:blue' for n in graph.nodes])
            plt.draw()
            plt.pause(1)


# generate the graphs
class Generate_Graphs: 

    def generate_connected_graph(self,n,m): 
        while True: 
            graph = nx.gnm_random_graph(n,m)
            if nx.is_connected(graph): 
                return graph



# Initialize the graph. 
graph = Generate_Graphs().generate_connected_graph(8,7)
# for line in nx.generate_adjlist(graph): 
#     print(line)
positions = nx.spring_layout(graph)

Visualize().visualize_search(order=DFS(graph).dfs_recursive_pre(0),positions=positions, title='Recursive DFS Algorithm',graph=graph)
