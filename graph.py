import shlex
import sys
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
		if vizinho in self.adjascentes.keys():
			return self.adjascentes[vizinho]
		else:
			return float("inf")
			# float("inf") vai criar um número infinito

	def adicionaArco(self, vizinho, peso):
		self.adjascentes[vizinho] = float(peso)


class Graph:
	def __init__(self, file = None):
		self.vertices = {}
		self.arestas = 0
		if file != None:
			f = open(file, "r")
			f1 = f.readlines()
			n = int(f1[0].split()[-1])

			for i in range(1, n+1):
				id, rotulo = shlex.split(f1[i])
				#print(id, rotulo)
				self.adicionaVertice(int(id), rotulo)

			op = f1[n+1]
			print(op)
			for line in f1[n+2:]:
				v1, v2, peso = line.split()
				#print(v1, v2, peso)
				if(op == "*arcs"):
					self.getVertice(v1).adicionaArco(int(v2), peso)
				else:
					self.adicionaAresta(int(v1), int(v2), peso)

	def getVertice(self, id):
		return self.vertices[id]

	def qtdVertices(self):
		return len(self.vertices)

	def qtdArestas(self):
		return self.arestas

	def adicionaVertice(self, id, rotulo):
		novo = Vertice(id, rotulo)
		self.vertices[id] = novo

	def adicionaAresta(self, v1, v2, peso):
		self.vertices[v1].adicionaArco(v2, peso)
		self.vertices[v2].adicionaArco(v1, peso)
		self.arestas += 1

	def haAresta(self, v1, v2):
		return v1 in self.vertices[v2].adjascentes and v2 in self.vertices[v1].adjascentes

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Use: ./" +sys.argv[0] + " [Nome do Arquivo]")
	else:
		Graph(sys.argv[1])