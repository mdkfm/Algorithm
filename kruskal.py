from graph import Graph, Edges, weighted_graph

def kruskal(wgraph):
	edges = [edge for edge in wgraph.weights.keys()]
	edges.sort(key=lambda edge: wgraph.weights[edge])
	
	edges1 = Edges()
	span_tree = weighted_graph(wgraph.vertexs.values(), edges1, {})
	
	for edge in edges:
		span_tree.add_edge(edge)
		if span_tree.has_circle():
			span_tree.cut_edge(edge)
	return span_tree

