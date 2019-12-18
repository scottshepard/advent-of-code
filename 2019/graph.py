import networkx as nx
from matplotlib import pyplot as plt

DG = nx.DiGraph()

DG.add_node('A')
DG.add_node('ORE')
DG.add_weighted_edges_from([('ORE', 'A', 10)])

nx.draw(DG)
plt.savefig('graphy.png')



