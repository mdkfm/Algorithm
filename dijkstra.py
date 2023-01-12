from graph import Graph, Edges, weighted_graph

def dijkstra(wgraph, begin, end):
	path = {}
	d = {}
	l = [vertex for vertex in wgraph.vertexs.values()]
	for vertex in wgraph.vertexs.values():
		d[vertex] = float("inf")
	d[begin] = 0
	while l:
		l.sorted(key=lambda vertex: d[vertex], reverse=True)
		v = l.pop()
		for u in wgraph.ad_list(v):
			if d[v]+wgraph.weights[(v, u)] < d[u]:
				d[u] = d[v] + wgraph.weights[(v, u)]
				path[u] = v			
