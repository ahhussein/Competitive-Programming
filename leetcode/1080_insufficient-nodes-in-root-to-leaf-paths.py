# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if self.dfs(root, limit, 0) == "delete":
            return None
        return root
        
    def dfs(self, node, limit, pathLength):
        if not node:
            return
        
        pathLength += node.val
        
        # reached a leaf
        if not node.left and not node.right and pathLength < limit:
            return "delete"
    
        actions_taken_children = []
        if node.left:
            action = self.dfs(node.left, limit, pathLength)
            if action == 'delete':
                node.left = None
            actions_taken_children.append(action)
                
        if node.right:
            action = self.dfs(node.right, limit, pathLength)
            if action == 'delete':
                node.right = None
            actions_taken_children.append(action)

            
        
        if not actions_taken_children or "keep" in actions_taken_children:
            return "keep"
        
        if "delete" in actions_taken_children:
            return "delete"
        
            
        
            
        

