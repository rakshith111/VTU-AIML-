import random

import netgraph  # pip install netgraph
import networkx
import matplotlib.pyplot as plt

#from programs.astarex import Graph_nodes
color = ['r', 'g', 'b', 'y', 'c', 'm', 'k']

maingraph = networkx.DiGraph()
colors = dict()
graph1  = {
    
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1),('H', 7)] ,
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5),('J',3)],

}
for node, dirs in graph1.items():
    maingraph.add_node(node)
    for dir in dirs:
        print(dir)
        c = random.choice(color)
        maingraph.add_edge(node, dir[0],  weight=dir[1], color=c)
        colors[(node, dir[0])] = c
        '''
        creates a list of colors based on the colors of each edge
        {('A', 'B'): 'm', ('A', 'F'): 'y', ('B', 'C'): 'm', ('B', 'D'): 'c', ('C', 'D'): 'g', ('C', 'E'): 'r', ('D', 'C'): 'k', ('D', 'E'): 'r', 
        ('E', 'I'): 'k', ('E', 'J'): 'm', ('F', 'G'): 'k', ('F', 'H'): 'g', ('G', 'I'): 'k', ('H', 'I'): 'g', ('I', 'E'): 'y', ('I', 'J'): 'r'}
        '''


labels = networkx.get_edge_attributes(maingraph, 'weight')
'''
Creates a dictionary with the edge as the key and the weight as the value
{('A', 'B'): 6, ('A', 'F'): 3, ('B', 'C'): 3, ('B', 'D'): 2, ('F', 'G'): 1, ('F', 'H'): 7, ('C', 'D'): 1, ('C', 'E'): 5, 
('D', 'C'): 1, ('D', 'E'): 8, ('E', 'I'): 5, ('E', 'J'): 5, ('I', 'E'): 5, ('I', 'J'): 3, ('G', 'I'): 3, ('H', 'I'): 2}
'''
# decide on a layout
pos = networkx.layout.fruchterman_reingold_layout(maingraph)

# draw the graph
plot_instance = netgraph.InteractiveGraph(
    maingraph, node_positions=pos, node_labels=True, arrows=True, edge_labels=labels, edge_color=colors)

######## drag nodes around #########

# To access the new node positions:
node_positions = plot_instance.node_positions

plt.draw()
plt.show()
