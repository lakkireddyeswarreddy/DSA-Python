"""

Union find also known as Disjoint set Union is a powerful data structure that keeps track of the collection of disjoint sets.
It mainly perform two operations :
1. find(x) - returns the parent element of the set that x contains
2. union(x,y) - checks if x and y are on same sets, if they are same sets it's a cycle.
Not, we add the root element of lesser rank(less height) set as achild to the root element of higher rank(more height).
if both sets rank are same then we can add any root as praent to the other and then increase the root by 1.

This data structure is used for identifing the cycles in the undirected graphs.
Used in Kruskal's algorithm.
"""


class Unionfind:
    def __init__(self, n):
        self.parent=list(range(n)) # initially each element is it's own parent.
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    

    def union(self, x,y):
        
        parentx = self.find(x)
        parenty = self.find(y)

        if parentx == parenty:
            return # Cycle exists
        
        rank1 = self.rank[parentx]
        rank2 = self.rank[parenty]

        if rank1 > rank2:
            self.parent[parenty]=parentx
        elif rank1 < rank2:
            self.parent[parentx]=parenty
        else:
            self.parent[parentx]=parenty
            self.rank[parenty]+=1

        return True


