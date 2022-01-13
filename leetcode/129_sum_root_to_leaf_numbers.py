# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, node, total_sum):
        if not node:
            return 0
        
        total_sum = total_sum * 10 + node.val
        if not node.left and not node.right:
            return total_sum
        
        return self.dfs(node.left, total_sum) + self.dfs(node.right, total_sum)
