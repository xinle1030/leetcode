from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.maxDiff = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxAncestorDiff_agg(root, root.val, root.val)
        return self.maxDiff
    
    def maxAncestorDiff_agg(self, node: Optional[TreeNode], minVal: int, maxVal: int) -> None:
        if node:
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            self.maxDiff = max(self.maxDiff, maxVal - minVal)
            self.maxAncestorDiff_agg(node.left, minVal, maxVal)
            self.maxAncestorDiff_agg(node.right, minVal, maxVal)

mySol = Solution()
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
print(mySol.maxAncestorDiff(root))

mySol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(0)
root.right.right.left = TreeNode(3)
print(mySol.maxAncestorDiff(root))




