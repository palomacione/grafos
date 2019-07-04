from graph import *


def fortemente_conexas(g):
    (floresta1, tempo_f) = dfs(g)

    transpose_g = Graph()

    for v in g.vertices.keys():
        u = g.get_vertice(v)
        transpose_g.adiciona_vertice(int(v), u.get_rotulo())

    for v in g.vertices.keys():
        u = g.get_vertice(v)
        for adj in u.vizinhos():
            transpose_g.get_vertice(adj).adiciona_arco(v, u.peso(adj))

    floresta, tempo_f_t = dfs(transpose_g, tempo_f)

    return floresta


def dfs(g, f=None):
    visited = {x: False for x in g.vertices}
    tempo_f = {x: float("inf") for x in g.vertices}
    tempo = [0]
    floresta = []
    verticelist = []
    if f is not None:
        for idVertice, tempoVertice in f.items():
            verticelist.append((idVertice, tempoVertice))
        verticelist.sort(key=lambda x: x[1], reverse=True)
        verticelist = list(map(lambda x: x[0], verticelist))
    else:
        verticelist = g.vertices.keys()
    for u in verticelist:
        if not visited[u]:
            found = []
            dfs_visit(g, u, visited, tempo_f, found, tempo)
            if len(found) > 0:
                floresta.append(found)
    return floresta, tempo_f


def dfs_visit(g, v, visited, tempo_f, found, tempo):
    visited[v] = True
    found.append(v)
    tempo[0] += 1
    for u in g.get_vertice(v).vizinhos():
        if not visited[u]:
            dfs_visit(g, u, visited, tempo_f, found, tempo)
    tempo[0] += 1
    tempo_f[v] = tempo[0]


def main():
    filename = sys.argv[1]
    g = Graph(filename)

    floresta = fortemente_conexas(g)
    for e in floresta:
        print(", ".join(str(a) for a in e))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
