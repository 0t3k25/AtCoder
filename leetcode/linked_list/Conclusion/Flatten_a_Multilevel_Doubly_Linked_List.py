class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        self.__flatten(head)
        return head

    def __flatten(self, node: "Node") -> "Node":
        cur = node
        last = node  # 最後のnode追跡

        while cur:
            next_node = cur.next

            # 子リストが存在
            if cur.child:
                child_last = self.__flatten(cur.child)

                # 子リストを親リストに繋げる
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None

                child_last.next = next_node
                if next_node:
                    next_node.prev = child_last

                # 子リストの最後のノード更新
                last = child_last
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
