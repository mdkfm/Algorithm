from graph import Graph, Edges

def dfs_connect(graph, vertex):
	search_list = []
	for v in graph.ad_list(vertex):
		if v not in search_list:
			search_list.append()
