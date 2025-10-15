"""
Floyd Warshal algorithm is used for finding the shortest path between every pair of nodes.
It works by initializing the distance matrix, which is a 2 dimensional array of size V*V.
Where distance[i][j]=0 if i==j, 
distance[i][j]=infinity, if no edge
distance[i][j]= weight, if there is an edge.

Then we consider every vertex as an intermediate vertex and then caclulate the distance[i][j] as
distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j]) (k is intermediate vertex)

if the distance[i][j]<0 the there is a negative cycel in the graph.
"""

graph = {
    "A" : [("B",3), ("C",2), ("D",4)],
    "B" : [("D",1), ("A", 3)],
    "C" : [("D", 1), ("A", 2)],
    "D" : [("C",1),("B",1), ("A",4)]
}

def floyd_warshall(graph):
    dist = { i : element for i, element in enumerate(graph) }
    distance = list()
    for i in range(len(graph)):
        distance.append([ float('inf') for i in range(len(graph))])
        for j in range(len(graph)):
            if i==j:
                distance[i][j]=0
            else:
                start_vertex = dist[i]
                end_vertex = dist[j]
                for neighbour, weight in graph[start_vertex]:
                    if neighbour==end_vertex:
                        distance[i][j]=weight
    print(distance)
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if distance[i][k] != float('inf') and distance[k][j] != float('Inf'):
                    distance[i][j]=min(distance[i][j], distance[i][k] + distance[k][j])
        
        print(distance)

    return distance
    
print(floyd_warshall(graph))
