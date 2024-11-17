class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        self.__flatten(head)

        return head

    def __flatten(self, node):
        cur = last = node
        while cur:
            next_node = cur.next
            if cur.child:
                child_last = self.__flatten(cur.child)  # 子ノードの最後の要素を返す
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None

                if next_node:
                    child_last.next = next_node
                    next_node.prev = child_last

                last = child_last
                cur = child_last
            else:
                last = cur
                cur = next_node
        return last


# if not head:
#     return head
# cur = head
# while cur:
#     if cur.child:
#         child_first = cur.child
#         child = cur.child
#         while child.next:
#             child = child.next
#         child.next = cur.next
#         if child.next:
#             child.next.prev = child
#         cur.next = child_first
#         cur.child = None
#         child_first.prev = cur
#     cur = cur.next
# return head
