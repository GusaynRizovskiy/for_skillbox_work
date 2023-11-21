import networkx as nx
import matplotlib.pyplot as plt
graph = nx.Graph()
graph.add_node("A")
graph.add_nodes_from(["B","C","D","E","F"])
graph.add_edges_from([("A","B"),("A","C"),("C","B"),("B","F"),("F","D"),("B","E"),("A","F")])
nodes = graph.nodes()
edge = graph.edges()
nx.draw(graph, with_labels=True, node_color = "green",edge_color = "blue")
plt.show()
