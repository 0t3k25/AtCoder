class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        val = self.head
        while index > 0 and val is not None:
            val = val.next
            index -= 1
        if val is None:
            return -1
        return val.value

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        point = self.head
        # 空リスト
        if point is None:
            self.addAtHead(val)
            return

        # 最後のノードまで
        while point.next is not None:
            point = point.next
        point.next = Node(val)

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
        if point is None:
            return

        # 末尾に追加する場合
        if point.next is None and current_index + 1 == index:
            self.addAtTail(val)
            return

        # 通常の挿入処理
        point.next = Node(val, point.next)

    def deleteAtIndex(self, index: int) -> None:
        # indexが0なら先頭に追加
        if index == 0:
            if self.head is not None:  # リストが空でないことを確認
                self.head = self.head.next
            return

        point = self.head
        current_index = 0

        # 指定されたindexの一つ前の位置まで移動
        while current_index < index - 1 and point is not None:
            point = point.next
            current_index += 1

        if point is None or point.next is None:
            return

        # 通常の削除処理
        point.next = point.next.next


class Node:

    def __init__(self, val: int, next=None):
        self.value = val
        self.next = next
