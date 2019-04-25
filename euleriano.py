import sys
from graph import *
from collections import deque

def hierholzer(g):
    edges = []
    for v in g.vertices:
        for a in g.getVertice(v).vizinhos():
            edges.append((v, a));
    res = set(map(tuple, map(sorted, edges)))
    visited = {x: False for x in res}
    (r, ciclo) = buscarSubcicloEuleriano(g, 1, visited)
    if not r:
        return (False, None)
    else:
        if all(visited):
            return (True, ciclo)
        else:
            return (False, None)

def buscarSubcicloEuleriano(g, v, visited):
    ciclo = [v]
    t = v
    while True:
        shoultReturn = True
        vu = None
        u = None
        for neighbour in g.getVertice(v).vizinhos():
            u = neighbour
            vu = tuple(sorted((v, u)))
            if not visited[vu]:
                shoultReturn = False
                break
        if shoultReturn:
            return (False, None)
        else:
            visited[vu] = True
            v = u
            ciclo.append(v)
        if v == t:
            break;
    vPassed = set(ciclo)
    for x in vPassed:
        someNotVisited = False
        for neighbour in g.getVertice(x).vizinhos():
            vu = tuple(sorted((x, neighbour)))
            if not visited[vu]:
                someNotVisited = True
                break
        if not someNotVisited:
            continue
        (r, ciclo2) = buscarSubcicloEuleriano(g, x, visited)
        if not r:
            return (False, None)
        cicloTemp = ciclo
        ciclo = []
        inserted = False
        for i in cicloTemp:
            if i == x and not inserted:
                inserted = True
                ciclo.extend(ciclo2)
            else:
                ciclo.append(i)
    return (True, ciclo)

def main():
    fileName = sys.argv[1]
    g = Graph(fileName)

    found, cicle = hierholzer(g)
    if found:
        print(1)
        print(", ".join(map(str, cicle)))
    else:
        print(0)

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Use: ./" +sys.argv[0] + " [Nome do Arquivo]")
	else:
		main()
