import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(0, 10), (10, 101)])
print(G)

# G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
plt.savefig("path.png")
