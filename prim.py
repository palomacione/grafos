from collections import deque
from heapq import *
from time import time

from graph import *


def prim(g):
    distances = {x: float("inf") for x in g.vertices}
    previous_vertices = {
        x: None for x in g.vertices
    }
    vertice = list(g.vertices.keys())[0]
    distances[vertice] = 0

    vertices = list(g.vertices.keys())
    while vertices:
        current_vertex = min(vertices, key=lambda x: distances[x])
        vertices.remove(current_vertex)
        v = g.get_vertice(current_vertex)
        for neighbour in v.vizinhos():
            if neighbour not in vertices:
                continue
            prev = distances[neighbour]
            next_distance = v.peso(neighbour)
            if next_distance < prev:
                previous_vertices[neighbour] = current_vertex
                distances[neighbour] = next_distance
    return distances, previous_vertices


def prim2(g):
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
    start = time()
    distance, previous_vertices = prim(g)
    end = time()
    # print("%.20f" % (end - start))
    start = time()
    mins, previous_vertices2 = prim2(g)
    end = time()
    # print("%.20f" % (end - start))
    # print(distance)
    # print(previous_vertices)
    # print(previous_vertices2)
    # print(mins)
    # print(sum(distance.values()))
    print(sum(mins.values()))
    for v in g.vertices.keys():
        path, current_vertex = deque(), v
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.appendleft(current_vertex)
        print(str(v) + ": " + ", ".join(map(str, path)) + "; d=" + str(distance[v]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
