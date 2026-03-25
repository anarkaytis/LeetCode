# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subSum(self, partSum: int) -> None:
        self.maxProd = max(self.maxProd, (self.sum - partSum) * partSum)

    def treeWalk(self, root : Optional[TreeNode], callback: Optional[Collable[int, None]]) -> int:
        if root is None:
            return 0
        lSum = self.treeWalk(root.left, callback)
        rSum = self.treeWalk(root.right, callback)
        if callback is not None:
            callback(lSum)
            callback(rSum)
        return lSum + rSum + root.val

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 1000000000 + 7
        self.sum = self.treeWalk(root, None)
        self.maxProd = 0
        self.treeWalk(root, self.subSum)
        return self.maxProd % MOD
