import sys
from graph import *
from collections import deque

def hierholzer(g):
    visited = {x: False for x in range(g.qtdArestas)}
    (r, ciclo) = buscarSubcicloEuleriano(g, 1, visited)

    if not r:
        return (False, None)
    else
        if all(visited):
            return (True, ciclo)
        else
            return (False, None)

def buscarSubcicloEuleriano(g, v, visited):
    ciclo = [v]
    t = v
    while True:
        shoultReturn = True
        for neighbour in g.getVertice(v).vizinhos():
            if not visited[neighbour]:
                shoultReturn = False
        if shoultReturn:
            return (False, None)
        else

        if v == t:
            break;

def main():
    fileName = sys.argv[1]
    g = Graph(fileName)
    found, cile = hierholzer(g)
    if found:
        print(1)
        print(", ".join(map(str, cicle)))
    else
        print(0)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Use: ./" +sys.argv[0] + " [Nome do Arquivo]")
	else:
		main()
