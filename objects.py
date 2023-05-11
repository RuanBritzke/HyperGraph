from typing import Any


DEFAULT = "Nu"
NF = True
NA = False

class Vertex:

    def __init__(self, Vertex) -> None: 
        self.__vertex = Vertex
        self.__neighbours = list()

    def __repr__(self) -> str:
        return f"{self.__vertex.__class__.__name__}({self.__vertex})"

    def __hash__(self) -> int:
        return hash(self.__vertex)
    
    def __eq__(self, other: "Vertex") -> bool:
        return self.__vertex == other.get_vertex()

    def get_vertex(self):
        return self.__vertex
    
    def set_neighbour(self, other : "Vertex"):
        if self is other:
            raise Exception(f"Vertex can't loop to itself")
        if other in self.get_neighbours():
            return
        self.__neighbours.append(other)
        if self in other.get_neighbours():
            return
        other.set_neighbour(self)

    def set_neighbours(self, *others : "Vertex"): 
        for other in others:
            self.set_neighbour(other)

    def get_neighbours(self):
        return [neighbour for neighbour in self.__neighbours]

    def remove_relation(self, other : "Vertex"):
        return

    def __str__(self, level = 0) -> str:
        """
        Imprime a estrutura hierarquica dos objetos salvos na Árvore.
        """
        if self.get_neighbours():
            return f"{str(self.__vertex)} - {self.__neighbours}"
        return f"{str(self.__vertex)}"

class Graph:
    """ 
    Stores all vertices of interest, can't remove them after stored.
    """

    def __init__(self) -> None:
        self.__vertices = set()

    def __hash__(self) -> int:
        return hash(object.__repr__(self))

    def set_vertices(self, *vertices):
        vertix : Vertex
        for vertix in vertices:
            self.__vertices.add(vertix)
            for neighbour in vertix.get_neighbours():
                self.__vertices.add(neighbour)

    def get_vertices(self):
        return self.__vertices

    def show(self):
        for vertex in self.__vertices:
            print(vertex)

    def find(self, object : str):
        for vertex in self.__vertices:
            if str(vertex) == object:
                return vertex
        



class Chave(Vertex):
    
    def __init__(self, equipamento : str, nopx: int, estado: str) -> None:
        self.equipamento = equipamento.upper()
        self.nopx = nopx
        self.estado = estado
        super().__init__(f"{self.equipamento}_{self.nopx}")


    def __repr__(self) -> str:
        return f"{self.equipamento}_{self.nopx}"


class Condutor(Vertex):

    def __init__(self, codigo) -> None:
        self.codigo = codigo
        self.tipo = DEFAULT
        super().__init__(self.codigo)

    def __repr__(self) -> str:
        return f"{self.codigo} {self.tipo}"

class Subestacao(Vertex):

    def __init__(self, nome) -> None:
        self.nome = nome.upper()
        super().__init__(self.nome)

    def __repr__(self):
        return f"{self.nome}"