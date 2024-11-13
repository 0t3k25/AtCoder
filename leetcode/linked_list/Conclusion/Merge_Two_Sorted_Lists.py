# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = None
        if l1 and l2:
            if l1.val > l2.val:
                head = ListNode(l1.val)
                l1 = l1.next
            else:
                head = ListNode(l2.val)
                l2 = l2.next

        while l1 and l2:
            if l1.val > l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next

        while l1:
            head.next = ListNode(l1.val)
            l1 = l1.next
            head = head.next

        while l2:
            head.next = ListNode(l2.val)
            l2 = l2.next
            head = head.next

        return head
