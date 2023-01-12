class Edges():
	def __init__(self, *edges, has_direction=False):
		'''
		has_direction仅限关键字参数确定边是否有向，默认无向
		'''
		self.edges = []
		self.has_direction = has_direction
		if edges:
			for edge in edges:
				self.edges.append(edge)
	
	def __contains__(self, edge):
		if self.has_direction:
			return edge in self.edges
		else:
			u, v = edge
			return edge in self.edges or (v, u) in self.edges
	
	def __call__(self):
		return self.edges
	
	def __len__(self):
		return len(self.edges)
	
	def __iter__(self):
		yield from self.edges
		
	def add(self, *edges):
		for edge in edges:
			self.edges.append(edge)
		
	def cut(self, *edges):
		if self.has_direction:
			for edge in edges:
				self.edges.remove(edge)
		else:
			for edge in edges:
				try:
					self.edges.remove(edge)
				except:
					u, v = edge
					self.edges.remove((v, u))
					
					
class Graph():
	def __init__(self, vertexs: 'list', edges: 'Edges'):
		self.vertexs = {num:vertex for num, vertex in enumerate(vertexs)}
		self.vertex_id = {vertex:num for num, vertex in enumerate(vertexs)}
		self.vertex_num = len(vertexs)
		self.edges = edges
		self.edge_num = len(edges)
	
	def ad_matrix(self):
		'''
		return the adjacent matrix of the graph by the order of self.vertexs
		'''
		adjacency_matrix = [[0 for i in range(self.vertex_num)] for i in range(self.vertex_num)]
		for i in range(self.vertex_num):
			for j in range(self.vertex_num):
				if (self.vertexs[i], self.vertexs[j]) in self.edges:
					adjacency_matrix[i][j] = 1
		return adjacency_matrix
		
	def ad_list(self, vertex):
		'''
		return a list of adjacent vertexies
		'''
		adjacent_list = []
		for u in range(self.vertex_num):
			if (vertex, self.vertexs[u]) in self.edges:
				adjacent_list.append(self.vertexs[u])
		
		return adjacent_list
	
	def max_degree(self):
		if self.edges.has_direction:
			edges = Edges(self.edges, has_direction=False)
			graph = Graph(self.vertexs.values(), edges)
		return max(sum(l) for l in graph.ad_matrix())
	
	def add_vertex(self, vertexs):
		for vertex in vertexs:
			num = len(self.vertexs)
			self.vertexs[num] = vertex
		self.vertex_num += len(vertexs)
	
	# ~ def cut_vertex(self, vertexs):
	
	def add_edge(self, *edges):
		self.edges.add(*edges)
	
	def cut_edge(self, *edges):
		self.edges.cut(*edges)
	
	def has_circle(self):
		'''
		find circles in the graph by degree
		'''
		edges = Edges(*self.edges(), has_direction=self.edges.has_direction)
		c = Graph(self.vertexs.values(), edges)
		degree = [0 for i in range(c.vertex_num)]
		if c.edges.has_direction:
			for edge in c.edges():
				_, v = edge
				degree[c.vertex_id[v]] += 1
			while 0 in degree:
				for i in range(c.vertex_num):
					if degree[i] == 0:
						for u in c.ad_list(self.vertexs[i]):
							c.cut_edge((self.vertexs[i],u))
							degree[self.vertex_id[u]] += -1
							degree[i] = -1
		else:
			for edge in c.edges():
				u, v = edge
				degree[c.vertex_id[u]] += 1
				degree[c.vertex_id[v]] += 1
			while 1 in degree:
				for i in range(c.vertex_num):
					if degree[i] == 1:
						for u in c.ad_list(self.vertexs[i]):
							c.cut_edge((self.vertexs[i],u))
							degree[self.vertex_id[u]] += -1
							degree[i] = -1
		# ~ for n in range(c.vertex_num):
			# ~ for i in range(c.vertex_num):
				# ~ degree = 0
				# ~ edges = []
				# ~ for j in range(c.vertex_num):
					# ~ if j != i and c.vertexs[i] in c.ad_list(self.vertexs[j]):
						# ~ degree += 1
						# ~ edges.append((c.vertexs[j], self.vertexs[i]))
				# ~ if edges:
					# ~ if not c.edges.has_direction and degree == 1:
						# ~ c.cut_edge(*edges)
					# ~ elif c.edges.has_direction and degree == 0:
						# ~ c.cut_edge(*edges)
		if len(c.edges):
			return True
		else:
			return False
		

class weighted_graph(Graph):
	def __init__(self, vertexs:'list', edges:'Edges', weights:'dict'):
		self.vertexs = {num:vertex for num, vertex in enumerate(vertexs)}
		self.vertex_id = {vertex:num for num, vertex in enumerate(vertexs)}
		self.vertex_num = len(vertexs)
		self.edges = edges
		if edges.has_direction:
			self.weights = weights
		else:
			self.weights = {}
			for edge, weight in weights.items():
				u, v = edge
				self.weights[(u, v)] = weight
				self.weights[(v, u)] = weight
				
	def add_weight(self, weights):
		for edge, weight in weights:
			self.weights[edge] = weight
