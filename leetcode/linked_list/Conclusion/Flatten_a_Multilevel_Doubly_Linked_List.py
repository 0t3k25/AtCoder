"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head
        cur = head
        while cur:
            if cur.child:
                child_first = cur.child
                child = cur.child
                while child.next:
                    child = child.next
                child.next = cur.next
                if child.next:
                    child.next.prev = child
                cur.next = child_first
                child_first.prev = cur
            cur = cur.next
        return head
