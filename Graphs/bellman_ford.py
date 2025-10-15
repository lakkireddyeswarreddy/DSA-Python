"""
Bellman Ford algorithm is used to find the shortest path from any source to remaining vertex even if the graph contains negative weights.
It initializes the distance dictionary with values infinity for all vertexs except source, for source it is 0.
Then for V-1 times iteratively.
For every edge
edge=(u,v)
if dist[u] + w (weight between u & v) < dist[v], upadte dist[v] = dist[u] + weight

if we relax any edge in the Vth iteration, then there exists a negative cycle in the graph
"""

graph = {
    "A" : [("B", 4), ("C", 3)],
    "B" : [("C", -1)],
    "C" : [("D", 2)],
}

negative_graph = {
    "A" : [("B",1)],
    "B" : [("C",2)],
    "C" : [("A", -4)]
}

from collections import defaultdict

def default_distance_value():
    return float('inf')

def bellman_ford(graph, source):
    distance = defaultdict(default_distance_value)
    distance[source] = 0

    for i in range(len(graph)-1):
        for vertex in graph:
            for neighbour, weight in graph[vertex]:
                if distance[vertex] != float('inf')  and distance[vertex] + weight < distance[neighbour]:
                    distance[neighbour] = distance[vertex] + weight

    for vertex in graph:
        for neighbour, weight in graph[vertex]:
            if distance[vertex] != float('inf')  and distance[vertex] + weight < distance[neighbour]:
                return True
            
    return distance

# print(bellman_ford(graph,"A"))
print(bellman_ford(negative_graph,"A"))


