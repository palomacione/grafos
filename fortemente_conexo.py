from graph import *


def fortemente_conexas(g):
    tempo_f = dfs(g)

    transpose_g = Graph()

    for v in g.vertices.keys():
        u = g.get_vertice(v)
        transpose_g.adiciona_vertice(int(v), u.get_rotulo())

    for v in g.vertices.keys():
        u = g.get_vertice(v)
        for adj in u.vizinhos():
            transpose_g.get_vertice(adj).adiciona_arco(v, u.peso(adj))

    floresta = get_strongly_connected_components(transpose_g, tempo_f)

    return floresta


def get_strongly_connected_components(g, tempo_f):
    verticelist = []
    for idVertice, tempoVertice in tempo_f.items():
        verticelist.append((idVertice, tempoVertice))
    verticelist.sort(key=lambda x: x[1], reverse=True)
    verticelist = list(map(lambda x: x[0], verticelist))
    visited = {x: False for x in g.vertices}
    tempo_f = {x: float("inf") for x in g.vertices}
    tempo = [0]
    floresta = []
    for v in verticelist:
        if not visited[v]:
            found = []
            dfs_visit(g, v, visited, tempo_f, found, tempo)
            if len(found) > 0:
                floresta.append(found)
    return floresta

def dfs(g):
    visited = {x: False for x in g.vertices}
    tempo_f = {x: float("inf") for x in g.vertices}
    tempo = [0]
    verticelist = g.vertices.keys()
    for u in verticelist:
        if not visited[u]:
            dfs_visit(g, u, visited, tempo_f, [], tempo)
    return tempo_f


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
    print(floresta)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
