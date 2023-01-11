from graph import Edges, Graph, weighted_graph
from kruskal import kruskal

edges = Edges((1,3), (1,4), (1,5), (1,6), (2,3), (2,4), (2,5), (3,4), (4,5), (4,6), (5,6))
weights = {edge:weight for edge, weight in zip(edges, [3, 10, 9, 9, 4, 2, 9, 3, 8, 9, 6])}
graph = weighted_graph(list(range(1, 7)), edges, weights)
span_tree = kruskal(graph)
for i in span_tree.ad_matrix():
	print(i)

