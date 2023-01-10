class Edges():
	def __init__(self, *edges, has_direction=False):
		'''
		has_direction仅限关键字参数确定边是否有向，默认无向
		'''
		self.edges = set()
		self.origin_edges = []
		self.has_direction = has_direction
		if edges:
			for edge in edges:
				self.origin_edges.append(edge)
				if self.has_direction:
					self.edges.add(edge)
				else:
					self.edges.add(frozenset(edge))
	
	def __contains__(self, edge):
		return frozenset(edge) in self.edges or edge in self.edges
	
	def __len__(self):
		return len(self.origin_edges)
	
	def __iter__(self):
		yield from self.origin_edges
		
	def add(self, *edges):
		for edge in edges:
			self.origin_edges.append(edge)
			if self.has_direction:
				self.edges.add(edge)
			else:
				self.edges.add(frozenset(edge))

class Graph():
	def __init__(self, vertex_num: 'int', edges: 'Edges'):
		'''
		vertex_num为顶点数， 顶点编号从1至vertexs
		'''
		self.vertex_num = vertex_num
		self.edges = edges
		self.edge_num = len(edges)
	
	def ad_matrix(self):
		'''
		返回图的邻接矩阵
		'''
		adjacency_matrix = [[0 for i in range(self.vertex_num)] for i in range(self.vertex_num)]
		for i in range(1, self.vertex_num+1):
			for j in range(1, self.vertex_num+1):
				if (i, j) in self.edges:
					adjacency_matrix[i-1][j-1] = 1
		return adjacency_matrix
		
	def ad_list(self, vertex):
		'''
		return a list of adjacent vertexies
		'''
		adjacent_list = []
		for u in range(1, self.vertex_num+1):
			if (vertex, u) in self.edges:
				adjacent_list.append(u)
		
		return adjacent_list
	
	def max_degree(self):
		#如果边有向则转化为无向，再用无向图的邻接矩阵求最大度
		graph = self
		if self.edges.has_direction:
			edges = Edges(*self.edges.origin_edges)
			graph = Graph(self.vertexs, edges)
		return max(sum(list) for list in graph.ad_matrix())
	
	def add_vertex(self, vertex_num):
		self.vertex_num += vertex_num
	
	def add_edge(self, *edges):
		self.edges.add(*edges)
		
	def has_circle(self):
		'''
		stackdfs
		'''
		if not seld.edges.has_direction and len(self.origin_edges) != set(self.oringin_edges):
			return True
		for edge in self.edges:
			u, v = edge
			if (v, u) in self.edges:
				return True
		visited_v = [0 for vertex in range(self.vertex_num)]
		for i in range(1, self.vertex_num+1):
			if visited[i-1] == 0:
				s = []
				instack = [0 for vertex in range(self.vertex_num)]
				s.append(i)
				instack[i-1] = 1
				while s:
					c = s.pop()
					instack[c-1] = 0
					visited[c-1] = 1
					for u in self.ad_list(c):
						if visited[u] == 0:
							s.append(u)
							instack[u-1] == 1
						elif instack[u-1] == 1:
							return True
		return False
	
class weight_edgraph(Graph):
	def __init__(self, vertex_num:'int', edges:'set of sets', weights:'dict'):
		self.vertex_num = vertex_num
		self.edges = edges
		self.weights = weights
	
	def add_weights(self, weights):
		for edge, weight in weights:
			self.weights[edge] = weight
