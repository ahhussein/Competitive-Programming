# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.helper(root, low, high)
        return root
    
        
    def helper(self, node, low, high):
        if not node:
            return None
        
        if node.val < low:
            return self.helper(node.right, low, high)
        
        elif node.val > high:
            return self.helper(node.left, low, high)
        
        node.left = self.helper(node.left, low, high) 
        node.right = self.helper(node.right, low, high) 
        return node
                
            
            
        
