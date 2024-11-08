# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 特殊ケース: リストが空または1つの要素しかない場合
        if not head or not head.next:
            return True

        slow = fast = head
        # 半分まで
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = (
            None,
            slow,
        )
        # 半分から後ろを反転
        while curr:
            curr.next, prev, curr = (
                prev,
                curr,
                curr.next,
            )  # 次のノードを保存 現在のノードのnextを反転 prevを現在のノードに移動 currを次のノードに移動

        # 回文をチェック
        left, right = head, prev  # `prev` は反転後のリストの先頭
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
