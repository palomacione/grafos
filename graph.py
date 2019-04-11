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
			#print(id, rotulo)
			self.adicionaVertice(int(id), rotulo)

		for line in f1[n+2:]:
			v1, v2, peso = line.split()
			#print(v1, v2, peso)
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
		self.vertices[v1].adicionaAresta(v2, peso)
		self.vertices[v2].adicionaAresta(v1, peso)
		self.arestas += 1

	def haAresta(self, v1, v2):
		return v1 in self.vertices[v2].adjascentes and v2 in self.vertices[v1].adjascentes

def buscaLargura(g, indice):
	visited = {}
	distance = {}
	predecessor = {}
	for v in g.vertices.keys():
		visited[v] = False
		distance[v] = float("inf")
		predecessor[v] = None

	visited[indice] = True
	distance[indice] = 0

	q = []
	q.append(indice)
	while len(q) > 0:
		u = q.pop(0)
		for n in g.getVertice(u).vizinhos():
			if not visited[n]:
				visited[n] = True
				distance[n] = distance[u] + 1
				predecessor[n] = u
				q.append(n)
	return (distance, predecessor)


def main():
	fileName = sys.argv[1]
	g = Graph(fileName)
	n = int(sys.argv[2])
	if n > g.qtdVertices() or n <= 0:
		print("O n tem que ser entre [1-" + str(g.qtdVertices()) + "]")
		return
	distance, predecessor = buscaLargura(g, n)
	level = {}
	for v in g.vertices.keys():
		if not distance[v] in level:
			level[distance[v]] = []
		level[distance[v]].append(v)
	for k in level.keys():
		print(str(k) + ": " + ", ".join(map(str, level[k])))

if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("Use: ./" +sys.argv[0] + " [Nome do Arquivo] [N° Vertice]")
	else:
		main()
