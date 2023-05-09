class Vertex:

    def __init__(self, Vertex) -> None: 
        self.__vertex = Vertex
        self.__neighbours = set()

    def __repr__(self) -> str:
        return f"{self.__vertex.__class__.__name__}({self.__vertex})"

    def __hash__(self) -> int:
        return hash(object.__repr__(self))
    
    def get_vertex(self):
        return self.__vertex

    def set_neighbours(self, *others : "Vertex"): 
        for other in others:
            if self is other:
                continue
            self.__neighbours.add(other)
            other.set_neighbours(self)
                
    def get_neighbours(self):
        return [neighbour for neighbour in self.__neighbours]


    def __str__(self, level = 0) -> str:
        """
        Imprime a estrutura hierarquica dos objetos salvos na Árvore.
        """
        spaces = "|   " * level
        prefix = spaces + "|-- " if level else ""
        print(prefix + str(self.__vertex))
        if self.get_neighbours():
            for neigbours in self.__neighbours:
                neigbours.__str__(level + 1)
            

class Graph:

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
