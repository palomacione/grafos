from heapq import *

from graph import *


def prim(g):
    previous_vertices = {
        x: None for x in g.vertices
    }
    vertice = list(g.vertices.keys())[0]
    q, mins, seen = [(0, vertice)], {vertice: 0}, set()
    while q:
        (last_cost, current_vertex) = heappop(q)
        seen.add(current_vertex)
        v = g.get_vertice(current_vertex)
        for neighbour in v.vizinhos():
            if neighbour in seen:
                continue
            prev = mins.get(neighbour)
            next_distance = v.peso(neighbour)
            if prev is None or next_distance < prev:
                previous_vertices[neighbour] = current_vertex
                mins[neighbour] = next_distance
                heappush(q, (next_distance, neighbour))
    return mins, previous_vertices


def main():
    filename = sys.argv[1]
    g = Graph(filename)
    mins, previous_vertices = prim(g)
    print(sum(mins.values()))
    for k, v in previous_vertices.items():
        if v is not None:
            print(str(k) + "-" + str(v) + ", ", end='');
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
