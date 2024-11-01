# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        is_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                is_cycle = True
                break
        if is_cycle is False:
            return None

        pos = 0
        slow = head
        while slow:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
            pos += 1
