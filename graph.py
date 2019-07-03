# -*- coding: utf-8 -*-

import shlex
import sys


class Vertice:
    def __init__(self, id_, rotulo):
        self.id = int(id_)
        self.rotulo = rotulo
        self.adjascentes = {}

    def vizinhos(self):
        return self.adjascentes.keys()

    def grau(self):
        return len(self.adjascentes)

    def get_rotulo(self):
        return self.rotulo

    def peso(self, vizinho, fluxo= False):
        if vizinho in self.adjascentes.keys():
            return self.adjascentes[vizinho]
        elif fluxo:
        	return 0
        else:
            return float("inf")
        # float("inf") vai criar um número infinito

    def adiciona_arco(self, vizinho, peso):
        self.adjascentes[(vizinho)] = float(peso)


class Graph:
    def __init__(self, file=None):
        self.vertices = {}
        self.arestas = 0
        self.s = 0
        self.t = 0

        if file is not None:
       	    ext = file.split('.')
            print(ext)
            f = open(file, "r", encoding='utf8')
            f1 = f.readlines()
            if ext[1] == "net":
	            n = int(f1[0].split()[-1])

	            for i in range(1, n + 1):
	                id_, rotulo = shlex.split(f1[i])
	                self.adiciona_vertice(int(id_), rotulo)
	            op = f1[n + 1].split()[0]
	            for line in f1[n + 2:]:
	                v1, v2, peso = line.split()
	                # print(v1, v2, peso)
	                if op == "*arcs":
	                    self.get_vertice(v1).adiciona_arco(int(v2), peso)
	                else:
	                    self.adiciona_aresta(int(v1), int(v2), peso)
            else:
	            for line in f1:
	                if line[0] == "c" or line[0] == "p":
	                    continue;
	                elif line[0] == "n":
	                    i = line.split()
	                    if i[2] == "s":
	                        self.s = i[1]
	                    else:
	                      	self.t = i[1]
	                elif line[0] == "a":
	                    a, v1, v2, peso = line.split()
	                    self.adiciona_vertice(int(v1), v1)
	                    self.adiciona_vertice(int(v2), v2)
	                    self.get_vertice(v1).adiciona_arco(self.get_vertice(v2), peso)
	                    print(v1, v2)
        print(self.vertices.keys())        
    def get_vertice(self, id_):
        return self.vertices[int(id_)]

    def qtd_vertices(self):
        return len(self.vertices)

    def qtd_arestas(self):
        return self.arestas

    def adiciona_vertice(self, id_, rotulo):
        novo = Vertice(id_, rotulo)
        self.vertices[id_] = novo

    def adiciona_aresta(self, v1, v2, peso):
        self.vertices[int(v1)].adiciona_arco(v2, peso)
        self.vertices[int(v2)].adiciona_arco(v1, peso)
        self.arestas += 1

    def ha_aresta(self, v1, v2):
        return v1 in self.vertices[v2].adjascentes and v2 in self.vertices[v1].adjascentes


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: ./" + sys.argv[0] + " [Nome do Arquivo]")
    else:
        Graph(sys.argv[1])
