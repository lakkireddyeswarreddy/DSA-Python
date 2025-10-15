"""
Graph is a non linear data structures, that consists of set of vertices, and set of edges connecting pairs of vertices.
Vertex is a fundamental unit of graph, often representing an object node.
Edge is a connection between any pair of vertices.
A graph is said to be directed, if the edges have directions(One Way).
A graph is said to be undirected, if the edges don't have direction(Bidirectional).
A graph is said to be weighted , if the weights are associated with the edges.
A graph is said to be unweighted, if the weights are not associated with the edges(Same weight for every edge).
A path is a sequence of edges connecting between the  any pair of vertices.
A graph is said to be connected,if in undirected graph there exist a path between any pair of vertices.
A graph is said to be strongly connected, if in directed graph there exists a path between any pair of vertices.
A graph is said to be cyclic, if there exists any path that starts and ends at the same vertex.
A graph is said to be acyclic, if it is not cyclic.
Degree of a vertex, number of edges incident to the vertex in undirected graph.
For directed we have in degree and out degree.

Tree is a connected, undirected, acyclic graph.
A graph is said to be complete, if there exists an direct edge between every pair of vertices.
Number of edges in a complete graph is n(n-1)/2
Edge connecting vertex with itself is known as self loop.

Grpaph can be represented as many ways :

1. Adjacency Matrix : A two dimensional matrix with size V*V, where V represents the no.of.vertices, and the value matrix[i][j] represents whether there is an edge between the vertices.
If there is no edge value : 0
else : 1 (unweighted) any value (weighted).

2. Adjacent list : An array of lists, where index represents the vertex and the list in the index represents the neighbours.

3. Edge List : List of all the edges in tuples (x,y,weight(if weighted)) else (x,y)

4. Incidence Matrix : A 2 dimensional matrix, where rows represent the vertex and the columns represents the edges.
if the value matrix[i][j] is greater than 0 then the edge is incident to the vertex.

Bipartite Graph
Vertices can be divided into two disjoint sets where edges only connect vertices from different sets.

"""
from collections import defaultdict
from collections import deque
class Graph:

    def __init__(self, weighted=False, directed=False):
        self.adjacency_list = defaultdict(list)
        self.weighted = weighted
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex]=list()

    def add_edge(self, v1, v2, weight=1):
        self.add_vertex(v1)
        self.add_vertex(v2)
        if self.weighted:
            self.adjacency_list[v1].append((v2,weight))
            if not self.directed:
                self.adjacency_list[v2].append((v1, weight))
        else:
            self.adjacency_list[v1].append(v2)
            if not self.directed:
                self.adjacency_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if not self.weighted:
            if v2 in self.adjacency_list[v1]:
                self.adjacency_list[v1].remove(v2)
                if not self.directed and v1 in self.adjacency_list[v2]:
                    self.adjacency_list[v2].remove(v1)

        else:
            self.adjacency_list[v1]=[neighbour for neighbour in self.adjacency_list[v1] if neighbour[0]!=v2]
            if not self.directed:
                self.adjacency_list[v2]=[neighbour for neighbour in self.adjacency_list[v2] if neighbour[0]!=v1]

    def get_vertices(self):
        return list(self.adjacency_list.keys())
    
    def get_edges(self):
        result=[]
        if not self.weighted:
            for vertex in self.adjacency_list:
                for neighbour in self.adjacency_list[vertex]:
                    if not self.directed and vertex > neighbour:
                        continue
                    result.append((vertex,neighbour))
        else:
            for vertex in self.adjacency_list:
                for neighbour, weight in self.adjacency_list[vertex]:
                    if not self.directed and vertex> neighbour:
                        continue
                    result.append((vertex,neighbour,weight))

        return result
    
    def get_degree(self, vertex):
        return len(self.adjacency_list[vertex])
    
    def bfs(self, vertex):
        visited = set()
        result=[]
        queue = deque([vertex])

        while queue:
            vertex = queue.popleft()
            visited.add(vertex)
            result.append(vertex)

            for neighbour in self.adjacency_list[vertex]:
                if self.weighted:
                    if neighbour[0] not in visited:
                        queue.append(neighbour[0])
                else:
                    if neighbour not in visited:
                        queue.append(neighbour)

        return result
    
    def dfs(self, vertex):
        visited = set()
        result = []

        def dfs_traversal(self,vertex):
            visited.add(vertex)
            result.append(vertex)
            neighbours = [neighbour[0] if self.weighted else neighbour for neighbour in self.adjacency_list[vertex]]
            for neighbour in neighbours:
                if neighbour not in visited:
                    dfs_traversal(self, vertex)

        dfs_traversal(self, vertex)
        return result
    

    def has_path(self, v1, v2):
        visited = set()

        def dfs_traversal(vertex):
            if vertex==v2:
                return True
            
            visited.add(vertex)
            neighbours = [neighbour[0] if self.weighted else neighbour for neighbour in self.adjacency_list[vertex]]
            for neighbour in neighbours:
                if neighbour not in visited and dfs_traversal(neighbour):
                    return True
            return False

        return dfs_traversal(v1)
    
    def shortest_path_unweighted(self, v1, v2):
        visited = set()
        parent_dict = dict({v1 : None})
        queue = deque([v1])

        while queue:
            vertex = queue.popleft()
            visited.add(vertex)
            if vertex==v2:
                path = []
                while vertex:
                    path.append(vertex)
                    vertex=parent_dict[vertex]
                return path[::-1]
            
            neighbours = [neighbour[0] if self.weighted else neighbour for neighbour in self.adjacency_list[vertex]]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
                    parent_dict[neighbour]=vertex


        return None
    




