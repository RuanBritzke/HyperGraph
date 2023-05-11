from objects import Vertex, Chave, Condutor, Graph

a = Chave(1008)
b = Condutor("XPLE")
c = Condutor("Multiplex")

a.set_neighbours(b, c)

A = Graph()
A.set_vertices(a)
print(A.get_vertices())