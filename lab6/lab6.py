import time
import networkx as nx
import matplotlib.pyplot as plt
import fw as f
import cam as c

G = nx.DiGraph()

# Reading adjacency matrix from file & saving it in "graph"
with open('graph.txt', 'r') as inputs:
    global graph
    graph = []

    for line in inputs:
        graph.append(line[:-1].split(', '))

G.add_weighted_edges_from(c.convert_adjacency_matrix(graph))

pos = nx.planar_layout(G)
nx.draw(G, with_labels='True', pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
start_time = time.time()
path = f.fw(graph, 0, 7)
end_time = time.time() - start_time
print(path)
print ('Вермя выполнения: ', '%.6f' %end_time,"sec")
path = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_edges(G, pos=pos, edgelist=path, edge_color='red')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.show()
