# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 0:
            return None
        val, idx = max((val, idx) for idx, val in enumerate(nums))
        node = TreeNode(val)
        node.left = self.constructMaximumBinaryTree(nums[: idx])
        node.right = self.constructMaximumBinaryTree(nums[idx + 1 :])
        return node
