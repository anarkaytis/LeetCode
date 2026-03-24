# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeWalk(self, root: Optional[TreeNode], values: List[TreeNode]) -> None:
        if root is None:
            return
        self.treeWalk(root.left, values)
        values.append(root)
        self.treeWalk(root.right, values)
    
    def treeBST(self, values: List[TreeNode], l: int, r: int) -> Optional[TreeNode]:
        if l >= r:
            return None
        m = (l + r) // 2
        node = values[m]
        node.left = self.treeBST(values, l, m)
        node.right = self.treeBST(values, m + 1, r)
        return node

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []
        self.treeWalk(root, values)
        return self.treeBST(values, 0, len(values))
