# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur, p1 = head, head.next
        head.next = None
        while p1:
            p1.next, cur, p1 = cur, p1, p1.next
        return cur
