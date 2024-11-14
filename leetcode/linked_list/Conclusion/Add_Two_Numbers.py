# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy
        carry: int = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            current.next = ListNode(sum % 10)
            carry = sum // 10
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            sum = l1.val + carry
            current.next = ListNode(sum % 10)
            carry = sum // 10
            current = current.next
            l1 = l1.next

        while l2:
            sum = l2.val + carry
            current.next = ListNode(sum % 10)
            carry = sum // 10
            current = current.next
            l2 = l2.next

        while carry:
            current.next = ListNode(carry % 10)
            carry = carry // 10

        return dummy.next
