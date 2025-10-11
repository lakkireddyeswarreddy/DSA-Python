"""
A tree is siad to be a BST, for any node in the tree, all the node values in the left sub tree are less than the nodes value and all the node values in the right sub tree are greater than the nodes value.

"""

class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        
root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(7)
root.left.left=TreeNode(2)
root.left.right=TreeNode(4)
root.right.right=TreeNode(8)


def is_valid_bst(root, min_val=float('-inf'),max_val=float('inf')):
    
    if not root:
        return True
    
    stack=[(root,min_val,max_val)]
    
    while stack:
        node, min_val, max_val = stack.pop()
        
        if not (min_val < node.val < max_val):
            return False
        
        if node.right:
            stack.append((node.right,node.val,max_val))
        
        if node.left:
            stack.append((node.left,min_val,node.val))
            
            
    return True
    
    
    # if not (min_val < root.val < max_val):
    #     return False
    
    # return is_valid_bst(root.left,min_val,root.val) and is_valid_bst(root.right,root.val,max_val)

print(is_valid_bst(root))


def delete_node(root,key):
    if not root:
        return None
    
    if key<root.val:
        root.left = delete_node(root.left,key)
    elif key>root.val:
        root.right = delete_node(root.right, key)
    else:
        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp=root.right
            while temp.left:
                temp=temp.left
            root.val=temp.val
            root.right=delete_node(root.right,temp.val)
            
    return root.val

print(delete_node(root,5))