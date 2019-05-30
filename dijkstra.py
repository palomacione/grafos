from graph import *
from collections import deque


def dijkstra(g, s):
    distances = {x: float("inf") for x in g.vertices}
    previous_vertices = {
        x: None for x in g.vertices
    }
    distances[s] = 0
    vertices = list(g.vertices.keys())
    while vertices:
        current_vertex = min(vertices, key=lambda x: distances[x])
        vertices.remove(current_vertex)
        if distances[current_vertex] == float("inf"):
            break
        v = g.get_vertice(current_vertex)
        for neighbour in v.vizinhos():
            cost = v.peso(neighbour)
            alternative_route = distances[current_vertex] + cost
            if alternative_route < distances[neighbour]:
                distances[neighbour] = alternative_route
                previous_vertices[neighbour] = current_vertex
    return distances, previous_vertices


def main():
    filename = sys.argv[1]
    g = Graph(filename)
    n = int(sys.argv[2])
    if n > g.qtd_vertices() or n <= 0:
        print("O n tem que ser entre [1-" + str(g.qtd_vertices()) + "]")
        return
    distance, previous_vertices = dijkstra(g, n)
    for v in g.vertices.keys():
        path, current_vertex = deque(), v
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.appendleft(current_vertex)
        print(str(v) + ": " + ", ".join(map(str, path)) + "; d=" + str(distance[v]))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo] [N° Vertice]")
    else:
        main()
