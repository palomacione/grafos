from graph import *


def hierholzer(g):
    edges = []
    for v in g.vertices:
        for a in g.get_vertice(v).vizinhos():
            edges.append((v, a))
    res = set(map(tuple, map(sorted, edges)))
    visited = {x: False for x in res}
    (r, ciclo) = buscar_subciclo_euleriano(g, 1, visited)
    if not r:
        return False, None
    else:
        if all(visited):
            return True, ciclo
        else:
            return False, None


def buscar_subciclo_euleriano(g, v, visited):
    ciclo = [v]
    t = v
    while True:
        shoult_return = True
        vu = None
        u = None
        for neighbour in g.get_vertice(v).vizinhos():
            u = neighbour
            vu = tuple(sorted((v, u)))
            if not visited[vu]:
                shoult_return = False
                break
        if shoult_return:
            return False, None
        else:
            visited[vu] = True
            v = u
            ciclo.append(v)
        if v == t:
            break
    v_passed = set(ciclo)
    for x in v_passed:
        some_not_visited = False
        for neighbour in g.get_vertice(x).vizinhos():
            vu = tuple(sorted((x, neighbour)))
            if not visited[vu]:
                some_not_visited = True
                break
        if not some_not_visited:
            continue
        (r, ciclo2) = buscar_subciclo_euleriano(g, x, visited)
        if not r:
            return False, None
        ciclo_temp = ciclo
        ciclo = []
        inserted = False
        for i in ciclo_temp:
            if i == x and not inserted:
                inserted = True
                ciclo.extend(ciclo2)
            else:
                ciclo.append(i)
    return True, ciclo


def main():
    file_name = sys.argv[1]
    g = Graph(file_name)

    found, cicle = hierholzer(g)
    if found:
        print(1)
        print(", ".join(map(str, cicle)))
    else:
        print(0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        main()
