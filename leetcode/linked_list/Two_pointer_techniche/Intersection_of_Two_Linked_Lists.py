# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        tmpA, tmpB = headA, headB

        while tmpA != tmpB:
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA

        return tmpA
        # bad sloution O(m*n)
        # while headA is not None:
        #     headB_pointer = headB
        #     while headB_pointer is not None:
        #         if headA == headB_pointer:
        #             return headB_pointer
        #         if headB_pointer.next is not None:
        #             headB_pointer = headB_pointer.next
        #         else:
        #             break
        #     if headA.next is not None:
        #         headA = headA.next
        #     else:
        #         break

        # return None
