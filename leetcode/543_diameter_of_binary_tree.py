# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 543. Path Sum II: https://leetcode.com/problems/path-sum-ii/
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Diamter of T1 = max(Diameter of T1.left , Diameter of T1.right, longest path through T1.root
        # Longest path through a node = height of left + height of right + 1 (for root)
        # Calculate max height of a subtree
        return self.calculateDiameter(root)[1]

    def calculateDiameter(self, node):
        if node == None:
            # height, diameter
            return (0, 0)

        heightLeft, diamterLeft = self.calculateDiameter(node.left)
        heightRight, diamterRight = self.calculateDiameter(node.right)

        longestPath = heightLeft + heightRight
        totalDiameter = max(max(diamterLeft, diamterRight), longestPath)

        return (max(heightLeft, heightRight) + 1, totalDiameter)
