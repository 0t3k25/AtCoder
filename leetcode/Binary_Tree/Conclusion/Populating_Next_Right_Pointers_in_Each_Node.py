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
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        def helper(left, right):
            if not left or not right:
                return

            left.next = right
            helper(left.right, right.left)
            helper(left.left, left.right)
            helper(right.left, right.right)

        if not root:
            return

        helper(root.left, root.right)
        return root
