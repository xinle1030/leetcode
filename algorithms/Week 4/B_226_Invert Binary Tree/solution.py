"""
In this question we have to Invert the binary tree.
So we use Post Order Treversal in which first we go in Left subtree and then in Right subtree then we return back to Parent node.
When we come back to the parent node we swap it's Left subtree and Right subtree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root