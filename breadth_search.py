import sys
from graph import *

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
