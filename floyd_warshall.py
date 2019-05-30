from graph import *


def floyd_warshall(g):
    n_matriz = g.qtd_vertices()
    m = [[0 for j in range(n_matriz)]
         for i in range(n_matriz)]

    for v1 in g.vertices.values():
        for v2 in g.vertices.values():
            if v1 == v2:
                continue
            else:
                m[v1.id - 1][v2.id - 1] = float(v1.peso(v2.id))

    for line in m:
        print(line)

    print(" ")
    for k in range(n_matriz):
        for i in range(n_matriz):
            for j in range(n_matriz):
                m[i][j] = min(m[i][j], m[i][k] + m[k][j])

    for index, line in enumerate(m):
        m[index] = list(map(int, line))

    v = 1
    for line in m:
        print(str(v) + ":" " " + str(line).replace('[', '').replace(']', ''))
        v += 1


def main():
    filename = sys.argv[1]
    g = Graph(filename)
    floyd_warshall(g)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
