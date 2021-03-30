"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 116. Populating Next Right Pointers in Each Node: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque


class Solution:
    # Level order traversal
    # Right to left, right in a temp and connect to it in the next iteration if both nodes share same level
    def connect(self, root: 'Node') -> 'Node':
        prevNode = None

        queue = deque()

        if not root:
            return None

        queue.append(root)
        while queue:
            n = len(queue)

            for i in range(1, n + 1):
                node = queue.popleft()

                # first node in level
                if i != 1:
                    node.next = prevNode

                prevNode = node

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return root