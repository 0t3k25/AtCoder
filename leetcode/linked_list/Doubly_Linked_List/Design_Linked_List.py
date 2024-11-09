class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        point = self.head
        current_index = 0
        while current_index < index and point:
            point = point.next
            index += 1
        if not point:
            return -1
        return point.value

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        # indexが0なら先頭に追加
        if index == 0:
            self.addAtHead(val)
            return

        point = self.head
        current_index = 0

        # 指定されたindexの一つ前の位置まで移動
        while current_index < index - 1 and point is not None:
            point = point.next
            current_index += 1

        # indexがリストの長さより大きい場合は挿入せず終了
        if not point:
            return

        # 末尾に追加する場合
        if point.next is None and current_index + 1 == index:
            self.addAtTail(val)
            return

        # 通常の挿入処理
        new_node = Node(val, point, point.next)
        point.next.prev = new_node
        point.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        # indexが0なら先頭に追加
        if index == 0:
            if self.head:  # リストが空でないことを確認
                self.head = self.head.next
            if self.head:  # 更新後のリストが空でない
                self.head.prev = None
            return

        point = self.head
        current_index = 0

        # 指定されたindexの一つ前の位置まで移動
        while current_index < index - 1 and point is not None:
            point = point.next
            current_index += 1

        # indexがリストの長さより大きい場合は挿入せず終了
        if not point:
            return

        # 末尾に追加する場合
        if not point.next and current_index + 1 == index:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return

        # 通常の削除処理
        point.next = point.next.next
        if point.next:
            point.next.prev = point


class Node:

    def __init__(self, val: int, prev=None, next=None):
        self.value = val
        self.prev = prev
        self.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
