class TreeNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        
root=TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right=TreeNode(8)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.right.right.left=TreeNode(5)
root.right.right.right=TreeNode(1)

from collections import deque
nodes=deque()
def has_path_sum(root, target):
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == target
    
    current_target=target-root.val
    
        

# print(has_path_sum(root,22))
