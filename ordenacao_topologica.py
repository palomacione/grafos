# -*- coding: utf-8 -*-
from graph import *


def main():
    filename = sys.argv[1]
    g = Graph(filename)
    lista = dfs_ot(g)
    print(", ".join(str(e) for e in lista))


def dfs_ot(g):
    visited = {}
    tempo_i = {}
    tempo_f = {}

    for v in g.vertices.keys():
        visited[v] = False
        tempo_i[v] = float("inf")
        tempo_f[v] = float("inf")

    tempo = 0
    ot = []
    for u in g.vertices.keys():
        if not visited[u]:
            dfs_visit_ot(g, u, visited, tempo_i, tempo_f, tempo, ot)
    return ot


def dfs_visit_ot(g, v, visited, tempo_i, tempo_f, tempo, ot):
    visited[v] = True
    tempo += 1
    tempo_i[v] = tempo

    for c in g.get_vertice(v).vizinhos():
        if not visited[c]:
            dfs_visit_ot(g, c, visited, tempo_i, tempo_f, tempo, ot)

    tempo += 1
    tempo_f[v] = tempo
    ot.insert(0, g.get_vertice(v).get_rotulo())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
