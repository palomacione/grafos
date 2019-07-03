from graph import *
from pprint import pprint



def edmonds_karp(C, source, sink):

    n = len(C) # C is the capacity matrix
    F = [[0] * n for _ in range(n)]
    # residual capacity from u to v is C[u][v] - F[u][v]

    while True:
        path = bfs(C, F, source, sink)
        if not path:
            break
        # traverse path to find smallest capacity
        u,v = path[0], path[1]
        flow = C[u][v] - F[u][v]
        for i in range(len(path) - 2):
            u,v = path[i+1], path[i+2]
            flow = min(flow, C[u][v] - F[u][v])
        # traverse path to update flow
        for i in range(len(path) - 1):
            u,v = path[i], path[i+1]
            F[u][v] += flow
            F[v][u] -= flow
    return sum([F[source][i] for i in range(n)])

def bfs(C, F, source, sink):
    P = [-1] * len(C) # parent in search tree
    P[source] = source
    queue = [source]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                queue.append(v)
                if v == sink:
                    path = []
                    while True:
                        path.insert(0, v)
                        if v == source:
                            break
                        v = P[v]
                    return path
    return None

def main():
	g = Graph()
	g.adiciona_vertice(1, "1")
	g.adiciona_vertice(2, "2")
	g.adiciona_vertice(3, "3")
	g.adiciona_vertice(4, "4")
	g.get_vertice(1).adiciona_arco(g.get_vertice(2), 5)
	g.get_vertice(1).adiciona_arco(g.get_vertice(3), 10)
	g.get_vertice(2).adiciona_arco(g.get_vertice(3), 15)
	g.get_vertice(2).adiciona_arco(g.get_vertice(4), 20)
	g.get_vertice(3).adiciona_arco(g.get_vertice(4), 5)

	C = []
	for u in g.vertices.keys():
		l = []
		for v in g.vertices.keys():
			l.append(g.get_vertice(u).peso(g.get_vertice(v), True))
		C.append(l)

	pprint(C)
	print(edmonds_karp(C, 0, 3))
main()