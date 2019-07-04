from graph import *


def hopcroft_karp(g):
	D = {}
	mate = {}
	for v in g.vertices:
		D[v] = float("inf")
		mate[v] = None
	m = 0

	while BFS(g, mate, D):
		for x in g.vertices_x:
			if mate[x] == None:
				if DFS(g, mate, x, D):
					m = m + 1
	return (m, mate)

def BFS(g, mate, D):
	q = []
	for x in g.vertices_x:
		if mate[x] == None:
			D[x] = 0
			q.append(x)
		else:
			D[x] = float("inf")

	D[None] = float("inf")
	while q:
		x = q.pop(0)
		if D[x] < D[None]:
			for y in g.get_vertice(x).vizinhos():
				if D[mate[y]] == float("inf"):
					D[mate[y]] = D[x] + 1
					q.append(mate[y])

	return D[None] != float("inf")

def DFS(g, mate, x, D):
	if x != None:
		for y in g.get_vertice(x).vizinhos():
			if D[mate[y]] == D[x] + 1:
				if DFS(g, mate, mate[y], D):
					mate[y] = x
					mate[x] = y
					return True
		D[x] = float("inf")
		return False
	return True

def main():
	filename = sys.argv[1]
	g = BipartiteGraph(filename)
	m, mate = hopcroft_karp(g)
	print("Emparelhamento máximo:", m)
	print("Arestas:", mate)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
