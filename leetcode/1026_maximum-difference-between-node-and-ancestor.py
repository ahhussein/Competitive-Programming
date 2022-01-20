# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, root.val, root.val, 0)
        
    
    def helper(self, node: Optional[TreeNode], minAncestor, maxAncestor, maxDistance) -> int:
        maxDistance = max(abs(node.val - minAncestor), maxDistance)
        maxDistance = max(abs(node.val - maxAncestor), maxDistance)
        
        if node.val < minAncestor:
            minAncestor = node.val
        if node.val > maxAncestor:
            maxAncestor = node.val
        
        if node.left:
            maxDistance = max(self.helper(node.left, minAncestor, maxAncestor, maxDistance), maxDistance)
        if node.right:
            maxDistance = max(self.helper(node.right, minAncestor, maxAncestor, maxDistance), maxDistance)
        
        return maxDistance
