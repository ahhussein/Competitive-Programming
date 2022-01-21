class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = [[] for i in range(n)]
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)
        self.visited = {0}
        self.totalLength = 0
        self.helper(tree, hasApple, 0) 
        return self.totalLength
    
    def helper(self, tree, hasApple, node):
        applePath = False # track if path ends with apple and bubble back up
        appleSubtree = False # track if subtree has at least one apple
        for child in tree[node]:
            if child not in self.visited:
                self.visited.add(child)
                applePath = self.helper(tree, hasApple, child)
                appleSubtree = applePath or appleSubtree
            if applePath:
                self.totalLength += 2
        return hasApple[node] or applePath or appleSubtree
        
