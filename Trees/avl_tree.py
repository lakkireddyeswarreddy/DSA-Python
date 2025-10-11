"""
AVL named after it's inventors Adelson-Velsky and Landis is an self balancing binary search tree in which heigh difference between the left and right subtrees differ atmost by 1.
Height difference between the left and right sub tree of an nodes is known as balance factor.
It balances itself after insertions and deletions if there is an imbalance.
It balances using rotations.
we have four rotations :

1. Left rotation (when the right subtree is heavier)
2. Right rotation (when the left sub tree is heavier)
3. Left Right rotation (when the right child of left sub tree is heavier)
4. Right Left rotation. (when the left child of right sub tree is heavier)

AVL tree gurantess O(logn) time complexity for operations like search, insertion and deletion unlike BST, which may become unbalanced like skewed or degenrate tree.
It is more balanced than BST.

Higher constant factors due to rotations ( constant factors refer to extra work for maintaining the balance factor by rotations that doesn't affect time complexity)

"""


class AVLNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1
        self.balance_factor=0
     
def get_height(node):
    if not node:
        return 0
    return node.height
   

def get_balance_factor(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotation(x):
    y=x.left
    temp=y.right
    
    x.right=y
    y.left=temp
    
    x.height = 1 +max(get_height(x.left), get_height(x.right))
    y.height = 1 +max(get_height(y.left),get_height(y.right))
    
    return y


def left_rotation(x):
    y=x.right
    temp=y.left
    
    y.left=x
    x.right = temp
    
    x.height = 1 +max(get_height(x.left), get_height(x.right))
    y.height = 1 +max(get_height(y.left),get_height(y.right))
    
    return y

def insert_key(node, key):
    if not node:
        return AVLNode(key)
    
    if node.key == key:
        return # duplicates keys not allowed
    
    elif key<node.key:
        node.left = insert_key(node.left,key)
        
    else:
        node.right = insert_key(node.right, key)
        
    node.height = 1 + max(get_height(node.left),get_height(node.right))
    
    node.balance_factor= get_balance_factor(node)
    
    if node.balance_factor > 1 and key < node.left.key:
        right_rotation(node)
        
    elif node.balance_factor < -1 and key > node.right.key:
        left_rotation(node)
        
    elif node.balance_factor > 1 and key > node.left.key:
        node.left = left_rotation(node.left)
        right_rotation(node)
        
    elif node.balance_factor < -1 and key < node.right.key:
        node.right = right_rotation(node.right)
        left_rotation(node)
        
    return node