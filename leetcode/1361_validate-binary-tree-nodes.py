import queue
from collections import defaultdict
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = self.findRoot(n, leftChild, rightChild)
        if root is None:
            return False
        
        visited = set()
        
        q = queue.Queue()
        
        q.put(root)
        visited.add(root)
        while not q.empty():
            node = q.get()

            left_child = leftChild[node]
            if left_child != -1:
                if left_child in visited:
                    return False
                
                q.put(left_child)
                visited.add(left_child)
            
            right_child = rightChild[node]
            if right_child != -1:
                if right_child in visited:
                    return False
                
                q.put(right_child)
                visited.add(right_child)

                
        if len(visited) == n:
            return True
        return False
    
    def findRoot(self, n, leftChild, rightChild):
        nodes_incoming_edges = set()
        for i in range(n):
            nodes_incoming_edges.add(leftChild[i])
            nodes_incoming_edges.add(rightChild[i])
            
        for i in range(n):
            if i not in nodes_incoming_edges:
                return i
        return None
        
            
        
