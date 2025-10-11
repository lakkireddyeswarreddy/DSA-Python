"""
A binary tree is a tree, in which each node has atmost two childrens, left sub tree and right sub tree.

A binary tree is said to be full binary tree if the node has 0 or 2 childrens.

A binary tree is a complete binary tree if all the levels are completed filled, except possibly the last level, which is filled from left to right.

A binary tree is a perfect binary tree if all the internal nodes has 2 children and all the leaf nodes are at the same level.

A binary tree is a Balanced binary tree if the difference between the left and right sub tree is atmost 1, and the left and right sub tree must obey the rule.

A binary tree is a degenarate or skewed binary tree if the paerent node has only one children.

A binary tree is a binary search tree if all the left nodes to the left are less than that, and all the right nodes are greater than that.

Traversal techniques :

1. Pre-order (root, left, right)
2. In-order (left, root, right)
3. Post-order (left, right, root)
4. Level order (level by level starting from 1.)

Pre, In , Post uses stack for traversal and has O(n) time complexity as we need to reach every node exactly once.
They has O(h) space complexity, where h is the height of the tree. In worst case, where tree is skewed tree (height=number of node) it is O(n). In balanced trees it is O(logn)

Level order has O(n) time complexity similar to other traversals and O(w) space complexity, where w is the width of the level that has more number of nodes. For perfect binary tree it is O(n/2)=O(n)
"""