class Edges():
	def __init__(self, *edges, has_direction=False):
		'''
		has_direction仅限关键字参数确定边是否有向，默认无向
		'''
		self.edges = set()
		self.origin_edges = edges
		self.has_direction = has_direction
		for edge in edges:
			if self.has_direction:
				self.edges.add(edge)
			else:
				self.edges.add(frozenset(edge))
	
	def __contains__(self, edge):
		return frozenset(edge) in self.edges or edge in self.edges
	
	def __len__(self):
		return len(self.origin_edges)
		

class Graph():
	def __init__(self, vertexs: 'dict', edges: 'set of sets'):
		'''
		传入参数vertexs是一个键值对形式为int: '顶点代号'的字典，或者是一个代表顶点个数数字
		'''
		self.vertexs = vertexs
		if isinstance(vertexs, int):
			self.vertexs = {i: '' for i in range(1, vertexs+1)}
		self.edges = edges
	
	def ad_matrix(self):
		'''
		返回图的邻接矩阵
		'''
		adjacency_matrix = [[0 for i in range(len(self.vertexs))] for i in range(len(self.vertexs))]
		for i in self.vertexs.keys():
			for j in self.vertexs.keys():
				if (i, j) in self.edges:
					adjacency_matrix[i-1][j-1] = 1
		return adjacency_matrix	
	
	def max_degree(self):
		#如果边有向则转化为无向，再用无向图的邻接矩阵求最大度
		graph = self
		if self.edges.has_direction:
			edges = Edges(*self.edges.origin_edges)
			graph = Graph(self.vertexs, edges)
		return max(sum(list) for list in graph.ad_matrix())
				
	def v_num(self):
		#返回点的个数
		return len(self.vertexs)
	
	def e_num(self):
		#返回边数
		return len(self.edges)
	
class weightedgraph(Graph):
	def __init__(self, vertexs:'dict', edges:'set of sets', weights:'dict'):
		self.vertexs = vertexs
		self.edges = edges
		self.weights = weights

