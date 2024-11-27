from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        deque = deque([root])

        while deque:
            level = []
            node = deque.popleft()
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
