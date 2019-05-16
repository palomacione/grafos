import sys
from graph import *

def fortemente_conexas(g):
	(visited, tempo_i, predecessor, tempo_f) = dfs(g)

	gt = Graph()

	for v in g.vertices.keys():
		u = g.getVertice(v)
		gt.adicionaVertice(int(v), u.rotulo())

	for v in g.vertices.keys():
		u = g.getVertice(v)
		print(v)
		for adj in u.vizinhos():
			gt.getVertice(adj).adicionaArco(v, u.peso(adj))

	(visited_t, tempo_i_t, predecessor_t, tempo_f_t) = dfs(g, tempo_f)

	return predecessor_t

def dfs(g, f = None):
	visited = {}
	tempo_i = {}
	tempo_f = {}
	predecessor = {}
	for v in g.vertices.keys():
		visited[v] = False
		tempo_i[v] = float("inf")
		tempo_f[v] = float("inf")
		predecessor[v] = None


	tempo = 0
	l = []
	if f != None:
		for idVertice, tempoVertice in f.items():
			l.append((idVertice, tempoVertice))
		l.sort(key=lambda x: x[1], reverse=True)
		l = map(lambda x: x[0], l)
	else:
		l = g.vertices.keys()
	for u in l:
		if not visited[u]:
			dfs_visit(g, u, visited, tempo_i, predecessor, tempo_f, tempo)

	return (visited, tempo_i, predecessor, tempo_f)

def dfs_visit(g, v, visited, tempo_i, predecessor, tempo_f, tempo):
	visited[v] = True
	tempo += 1
	tempo_i[v] = tempo
	for u in g.getVertice(v).vizinhos():
		if not visited[u]:
			predecessor[u] = v
			dfs_visit(g, u, visited, tempo_i, predecessor, tempo_f, tempo)

	tempo += 1
	tempo_f[v] = tempo

def main():
	fileName = sys.argv[1]
	g = Graph(fileName)
	
	predecessor_t = fortemente_conexas(g)
	print(",".join(map(str, predecessor_t)))


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Use: ./" +sys.argv[0] + " [Nome do Arquivo]")
	else:
		main()
