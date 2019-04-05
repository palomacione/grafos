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
		if haAresta(self, vizinho):
			return self.adjascentes[vizinho]
		else:
			return float("inf") 
			# float("inf") vai criar um número infinito

	def adicionaAresta(self, vizinho, peso):
		self.adjascentes[vizinho] = peso


class Graph:
	def __init__(self, file):
		self.vertices = {}
		self.arestas = 0

		f = open(file, "r")
		f1 = f.readlines()
		n = int(f1[0].split()[-1])

		for i in range(1, n+1):
			id, rotulo = f1[i].split()
			print(id, rotulo)
			self.adicionaVertice(int(id), rotulo)

		for line in f1[n+2:]:
			v1, v2, peso = line.split()
			print(v1, v2, peso)
			self.adicionaAresta(int(v1), int(v2), peso)

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
