class Vertice:
	def __init__(self, id, rotulo):
		self.id = id
		self.rotulo = rotulo
		self.adjascentes = {}

	def vizinhos(self):
		return self.adjascentes.keys()

	def grau(self):
		return len(self.adjascentes)

	def rotulo(self):
		return self.rotulo

	def peso(self, vizinho):
		return self.adjascentes[vizinho]

	def adicionaAresta(self, vizinho, peso):
		self.adjascentes[vizinho] = peso


class Graph:
	def __init__(self):
		self.vertices = {}
		self.arestas = 0

	def __init__(self, file):
		self.__init__()
		f = open(file, "r")
		f1 = f.readlines()
		edges = False
		n = int(f1[0].split()[-1])
		for i in range(1, n+1):
			line = f1[i]
			self.adicionaVertice(int(line.split()[0]), line.split[1])

			



	def qtdVertices(self):
		return len(self.vertices)

	def qtdArestas(self):
		return self.arestas


	def adicionaVertice(self, id, rotulo):
		novo = Vertice(id, rotulo)
		self.vertices[id] = novo

	def adicionaAresta(self, v1, v2, peso):
		self.vertices[v1].adicionaAresta(self.vertices[v2], peso)
		self.vertices[v2].adicionaAresta(self.vertices[v1], peso)
		self.arestas += 1

	def haAresta(self, v1, v2):
		return self.vertices[v1] in self.vertices[v2].adjascentes and self.vertices[v2] in self.vertices[v1].adjascentes


