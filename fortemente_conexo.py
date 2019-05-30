from graph import *


def fortemente_conexas(g):
    (visited, tempo_i, predecessor, tempo_f) = dfs(g)

    transpose_g = Graph()

    for v in g.vertices.keys():
        u = g.get_vertice(v)
        transpose_g.adiciona_vertice(int(v), u.get_rotulo())

    for v in g.vertices.keys():
        u = g.get_vertice(v)
        for adj in u.vizinhos():
            transpose_g.get_vertice(adj).adiciona_arco(v, u.peso(adj))

    (visited_t, tempo_i_t, predecessor_t, tempo_f_t) = dfs(transpose_g, tempo_f)

    return predecessor_t


def dfs(g, f=None):
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
    verticelist = []
    if f is None:
        verticelist = g.vertices.keys()
    else:
        for idVertice, tempoVertice in f.items():
            verticelist.append((idVertice, tempoVertice))
        verticelist.sort(key=lambda x: x[1], reverse=False)
        verticelist = list(map(lambda x: x[0], verticelist))
    for u in verticelist:
        if not visited[u]:
            dfs_visit(g, u, visited, tempo_i, predecessor, tempo_f, tempo)

    return visited, tempo_i, predecessor, tempo_f


def dfs_visit(g, v, visited, tempo_i, predecessor, tempo_f, tempo):
    visited[v] = True
    tempo += 1
    tempo_i[v] = tempo
    for u in g.get_vertice(v).vizinhos():
        if not visited[u]:
            predecessor[u] = v
            dfs_visit(g, u, visited, tempo_i, predecessor, tempo_f, tempo)

    tempo += 1
    tempo_f[v] = tempo


def main():
    filename = sys.argv[1]
    g = Graph(filename)

    predecessor_t = fortemente_conexas(g)
    print(predecessor_t)
    floresta = {}
    root = {}
    for arv in predecessor_t.keys():
        raiz = None
        temp = arv
        if temp in root:
            continue
        arvores = set()
        while temp is not None:
            if temp in root:
                raiz = root[temp]
                break
            arvores.add(temp)
            raiz = temp
            temp = predecessor_t[temp]
        for node in arvores:
            root[node] = raiz
        if raiz not in floresta:
            floresta[raiz] = set()
        floresta[raiz].update(arvores)

    for values in floresta.values():
        print(values)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
