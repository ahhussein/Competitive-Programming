# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 113. Path Sum II: https://leetcode.com/problems/path-sum-ii/

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        self.results = []
        self.path = []
        if not root:
            return []

        self.path.append(root.val)
        self.backtrack(root, sum - root.val)
        return self.results

    def backtrack(self, node, remaining):
        if node == None:
            return

        if remaining == 0 and not node.left and not node.right:
            self.results.append(self.path[:])
            return True

        if node.left:
            self.path.append(node.left.val)
            self.backtrack(node.left, remaining - node.left.val)
            self.path.pop()

        if node.right:
            self.path.append(node.right.val)
            self.backtrack(node.right, remaining - node.right.val)
            self.path.pop()

#         finalPathsList = []

#         self.possiblePaths(root, sum, [], finalPathsList)

#         return finalPathsList

#     def possiblePaths(self, node, remainingSum, path, finalList):
#         if node is None:
#             return

#         remainingSum -= node.val
#         path.append(node.val)
#         if not node.left and not node.right and remainingSum == 0:
#             finalList.append(path)
#             return
#         if node.left:
#             self.possiblePaths(node.left, remainingSum, path[:], finalList)

#         if node.right:
#             self.possiblePaths(node.right, remainingSum, path[:], finalList)
