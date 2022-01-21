# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
import queue

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        tree = defaultdict(list)       
        
        # build tree as dict
        self.treeDict(root, tree)
        
        matchedNodes = []
        
        
        q = queue.Queue()
        q.put((target.val, 0))
        visited = set()

        while not q.empty():
            node, level = q.get()
            visited.add(node)
            if level == k:
                matchedNodes.append(node)
                continue
            
            for child in tree[node]:
                if child in visited:
                    continue
                q.put((child, level+1))

        return matchedNodes
            
        
    def treeDict(self, node, tree):
        if not node:
            return
        
        if node.left:
            tree[node.val].append(node.left.val)
            tree[node.left.val].append(node.val)
            self.treeDict(node.left, tree)            
        if node.right:
            tree[node.val].append(node.right.val)
            tree[node.right.val].append(node.val)
            self.treeDict(node.right, tree)    
        
        

