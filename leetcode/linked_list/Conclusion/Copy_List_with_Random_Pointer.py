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
        # hashmap
        # copy_dict = dict()
        # cur = head

        # while cur:
        #     copy_dict[cur] = Node(cur.val)
        #     cur = cur.next

        # cur = head
        # while cur:
        #     if cur.next:
        #         copy_dict[cur].next = copy_dict[cur.next]
        #     if cur.random:
        #         copy_dict[cur].random = copy_dict[cur.random]
        #     cur = cur.next
        # return copy_dict[head] if head else None

        # in place approach
        cur = head

        # nodeの間に挿入
        while cur:
            new_node = Node(cur.val, cur.next)
            cur.next = new_node

            cur = new_node.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = head
        pseudo_head = Node(0)  # コピーされたリストの先頭ダミーノード
        copy_cur = pseudo_head

        while cur:
            copy = cur.next
            cur.next = copy.next
            copy_cur.next = copy
            copy_cur = copy

            cur = cur.next
        # コピーリストの先頭を返す
        return pseudo_head.next
