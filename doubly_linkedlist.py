class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode

    def insertNode(self, value, location):
        if self.head is None:
            return
        newNode = Node(value)
        if location == 0:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        elif location == -1:
            newNode.next = None
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            index = 0
            temp = self.head
            while index < location - 1:
                index += 1
                temp = temp.next
            nextNode = temp.next
            nextNode.prev = newNode
            newNode.next = nextNode
            temp.next = newNode
            newNode.prev = temp


doublyLL = DoublyLinkedList()
doublyLL.createDLL(1)
doublyLL.insertNode(0, -1)
doublyLL.insertNode(0, 0)
doublyLL.insertNode(1, 1)

print([node.value for node in doublyLL])
