class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        point = self.head

        while point and index > 0:
            point = point.next
            index -= 1

        if not point:
            return -1

        return point.value

    def addAtHead(self, val: int) -> None:
        # create node
        new_node = Node(val)
        # confirm node
        if not self.head:  # empty
            self.tail = new_node
        else:
            new_node.next, self.head.prev = self.head, new_node

        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.tail:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail

        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        # first node
        if index == 0:
            self.addAtHead(val)
            return

        point = self.head

        while point and index > 0:
            point = point.next
            index -= 1

        # out of index
        if index > 0:
            return

        # last node
        if not point:
            self.addAtTail(val)
            return

        new_node = Node(val)
        new_node.prev = point.prev
        new_node.next = point
        point.prev.next = new_node
        point.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        # first node
        if index == 0 and self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        point = self.head

        while point and index > 0:
            point = point.next
            index -= 1

        # out of index
        if not point:
            return

        # last node
        if not point.next:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        point.prev.next = point.next
        point.next.prev = point.prev


class Node:
    def __init__(self, value: int):
        self.value = value
        self.prev = None
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
