class ListNode:
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addItem(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.pointer = item

        self.tail = item


singlyLinkedlist = SinglyLinkedList()
node1 = ListNode(15)
singlyLinkedlist.addItem(node1)
singlyLinkedlist.addItem(1)
singlyLinkedlist.addItem(True)

print(singlyLinkedlist)
print(singlyLinkedlist.head.value, singlyLinkedlist.tail.value)







