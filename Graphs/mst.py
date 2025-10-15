"""
A spanning tree is a subset of graph edges, that connect every vertex without forming the cycles and has exactly (v-1) edges.
A MST (minimum spanning tree)  is a spanning tree with minimum total edge weight.


Kruskal's algorithm is used to find the MST by sorting all the edges in non decreasing order by weight, and then adding the edges from smallest to largest untill the mst reaches length of V-1.

"""
from .union_find import Unionfind
edges_list=[(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]

def kruskals(n, edges):
    union_find = Unionfind(n)
    edges.sort(key=lambda x : x[2])
    mst=[]
    total_weight=0

    for source, destination, weight in edges:
        if union_find(source, destination):
            total_weight+=weight
            mst.append((source,destination,weight))
            if len(mst)==n-1:
                break

    return mst, total_weight

print(kruskals(4,edges_list))
