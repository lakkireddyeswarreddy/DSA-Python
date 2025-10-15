"""
Dijkstras algorithm is used to find the shortest path from single source to all other nodes in weighted graph with non negative edges.
It works by initializing a distance dict with infinity values for every vertex except the source, and 0 for the zero.
We use priority queue(min heap) for popping vertexs with minimum distance.
We start by placing source in the min heap


This algorithm doesn't works if we have negative edges, as it assumes if a vertex is visited it's shortest path is determined. But if we have negative edges the longest path may become shorter dur to negative weights.
For calculating the shortest path with negative edges we have Bellman - Ford algorithm.
"""



graph={

    "A" : [("B", 1), ("C", 4)],
    "B" : [("C", 2),("D", 5)],
    "C" : [("D",1)],
    "D" : []

}
import heapq
from collections import defaultdict

def default_distance_value():
    return float('inf')

def dijsktras(graph, source):
    distance=defaultdict(default_distance_value)
    distance[source]=0
    min_heap = []
    heapq.heappush(min_heap,(0,source))
    while min_heap:
        path_distance, vertex = heapq.heappop(min_heap)
        if path_distance > distance[vertex]:
            continue

        for neighbour, weight in graph[vertex]:
            vertex_distance = path_distance+weight
            if vertex_distance < distance[neighbour]:
                distance[neighbour]=vertex_distance
                heapq.heappush(min_heap,(vertex_distance,neighbour))

    return distance

print(dijsktras(graph,"A"))

