from graph import Graph, Edges, weigh_tedgraph

def kruskal(wgraph):
	edges = [edge for edge in wgraph.weights.keys()]
	edges.sort(key=lambda edge: wgraph.weights[edge])
	
	edges1 = Edges()
	span_tree = weighted_graph(wgraph.vertex_num, edges1, {})
	vertexs = set()
	
	for edge in edges:
		span_tree_i = span_tree.add_edges(edge)
		span_tree_i.add_weights(wgraph.weights[edge])
		if not span_tree_i.has_circle():
			span_tree = span_tree_i
	
	return span_tree

