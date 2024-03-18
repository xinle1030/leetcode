# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        sum = [0]
        return self.bstToGst_agg(root, sum)

    def bstToGst_agg(self, root: TreeNode, sum: int) -> TreeNode:
        if not root:
            return None
        self.bstToGst_agg(root.right, sum)

        sum[0] += root.val
        root.val = sum[0]

        self.bstToGst_agg(root.left, sum)

        return root

mySol = Solution()
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)

root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

print(mySol.bstToGst(root))



