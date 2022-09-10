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

    def traverseDLL(self):
        if self.head is None:
            return
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next

    def reverseTraversalDLL(self):
        if self.head is None:
            return
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev

    def searchDLL(self, nodeValue):
        if self.head is None:
            return False
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return True
            tempNode = tempNode.next
        return False

    def deleteNode(self, location):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if location == 0:
            nextNode = self.head.next
            nextNode.prev = None
            self.head = nextNode
        elif location == -1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            index = 0
            curNode = self.head
            while index < location - 1:
                index += 1
                curNode = curNode.next
            curNode.next.next.prev = curNode  # missing part
            curNode.next = curNode.next.next
            curNode.next.prev = None


doublyLL = DoublyLinkedList()
doublyLL.createDLL(1)
doublyLL.insertNode(0, -1)
doublyLL.insertNode(0, 0)
doublyLL.insertNode(1, 1)
doublyLL.insertNode(2, 1)
doublyLL.deleteNode(-1)
doublyLL.deleteNode(-2)
doublyLL.reverseTraversalDLL()

print([node.value for node in doublyLL])
