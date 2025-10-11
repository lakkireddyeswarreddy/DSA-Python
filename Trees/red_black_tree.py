"""
Red Black Tree is a type of self balancing binary search tree that enforces certain colouring rules for maintaining the balance. Every node in the red black tree takes extra bit for storing the colour of the node.
Properties of Red black tree are :
1. root node should be black.
2. All Nil nodes should be black
3. No two red nodes should be adjaceent
4. Number of black nodes from node to all it's descendant NIL nodes should be same, which is known as Black height of the node.
5. Each node should have either red or black colour.

Red Black tree also uses rotations for maintaining the properties.

We insert every new node as a red node

1. If the new node becomes root, then change the colour to black.
2. If the new node parent is black, no change.
3. if the new node praent is red and uncle(neighbour of parent node) is red, change the colur of parent and uncle to black and the colour of grandparent to red, and then fix the grand parent recursively as it may violated the no two red nodes should be adjacent property with it's parent node.
4. if the new node praent is rec and the neighbour is black, we perform rotations :
    a. one rotation if the grand parent and the new node are in straight line
    b. two rotations if they are not in straight line.
    
AVL tree is more strictly balanced than the RB tree which has height atmost 2log2(n+1) compared to O(logn) for AVL tree, so AVL tree is faster for lookups.
But RB tree is faster for insertion and deletions as we need to do less rotations than AVL tree.
RB tree are used in programming languages like C++ STL, java TreeMAp and for database indexing.
"""

class RBNode:
    def __init__(self, key, colour ="Red"):
        self.key = key
        self.left=None
        self.right=None
        self.parent=None
        self.colour = colour
        
        

def left_rotation(x):
    y=x.right
    x.right=y.left
    
    if not x.right:
        x.right.parent=x
        
    y.parent=x.parent
    
    if not x.parent:
        root=y
    elif x == x.parent.left:
        x.parent.left=y
    else:
        x.parent.right=y
        
    x.parent=y
    y.left=x
    
    return y


def right_rotation(x):
    y=x.left
    x.left=y.right
    y.right=x
    
    if not x.left:
        x.left.parent = x
        
    y.parent=x.parent
    
    if not x.parent:
        root=y
    elif x == x.parent.left:
        x.parent.left=y
    else:
        x.parent.right=y
        
    x.parent=y
    return y
        
        