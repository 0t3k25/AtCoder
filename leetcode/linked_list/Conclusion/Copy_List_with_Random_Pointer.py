"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        copy_dict = dict()
        cur = head

        while cur:
            copy_dict[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                copy_dict[cur].next = copy_dict[cur.next]
            if cur.random:
                copy_dict[cur].random = copy_dict[cur.random]
            cur = cur.next
        return copy_dict[head] if head else None
