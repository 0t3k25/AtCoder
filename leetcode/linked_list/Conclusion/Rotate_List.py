# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        list_size = 0

        # mesure list size
        while cur:
            list_size += 1
            cur = cur.next

        # calculate rotate count
        rotate_count = k % list_size

        last_num = list_size - rotate_count
        new_head = head
        if last_num != list_size:
            connect_list = head
            while last_num > 1:
                connect_list = connect_list.next  # 新しいヘッドの終点
                last_num -= 1
            new_head = connect_list.next
            connect_list.next = None
            cur = new_head
            while cur.next:
                cur = cur.next
            cur.next = head

        return new_head
