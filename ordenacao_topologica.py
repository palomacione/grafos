import sys
from graph import *

def main():
	fileName = sys.argv[1]
	g = Graph(fileName)
	lista = dfs_OT(g)
	print(", ".join(str(e) for e in lista))

def dfs_OT(g):
	visited = {}
	tempo_i = {}
	tempo_f = {}
	predecessor = {}

	for v in g.vertices.keys():
		visited[v] = False
		tempo_i[v] = float("inf")
		tempo_f[v] = float("inf")


	tempo = 0
	OT = []
	for u in g.vertices.keys():
		if not visited[u]:
			dfsVisitOT(g, u, visited, tempo_i, tempo_f, tempo, OT)
	return OT

def dfsVisitOT(g, v, visited, tempo_i, tempo_f, tempo, OT):
	visited[v] = True
	tempo += 1
	tempo_i[v] = tempo

	for c in g.getVertice(v).vizinhos():
		if not visited[c]:
			dfsVisitOT(g, c, visited, tempo_i, tempo_f, tempo, OT)

	tempo += 1
	tempo_f[v] = tempo
	OT.insert(0, g.getVertice(v).get_rotulo())

main()