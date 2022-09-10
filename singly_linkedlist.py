class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in SLL
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif location == 0:
            newNode.next = self.head
            self.head = newNode
        elif location == -1:
            self.tail.next = newNode
            self.tail = newNode
        else:
            index = 0
            tempNode = self.head
            while index < location - 1:
                index += 1
                tempNode = tempNode.next
            nextNode = tempNode.next
            tempNode.next = newNode
            newNode.next = nextNode

    def traverseSLL(self):
        if self.head == None:
            return
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next

    def searchSLL(self, nodeValue):
        if self.head == None:
            return
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return True
            tempNode = tempNode.next
        return False

    def deletNode(self, location):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if location == 0:
            self.head = self.head.next
        elif location == -1:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        else:
            temp = self.head
            index = 0
            while index < location - 1:
                index += 1
                temp = temp.next
            nextNode = temp.next
            temp.next = nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            return
        self.head = None
        self.tail = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail = node
        node.next = node
        return "CSLL was created"

    def insertCSLL(self, value, location):
        if self.head is None:
            return
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif location == -1:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            index = 0
            temp = self.head
            while index < location - 1:
                index += 1
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

    def traversalCSLL(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return True
            tempNode = tempNode.next
            if tempNode == self.head:
                break
        return False

    def deleteNode(self, location):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head.next = None
            self.tail = None
            self.head = None
        if location == 0:
            self.head = self.head.next
            self.tail.next = self.head
        elif location == -1:
            temp = self.head
            while temp:
                if temp.next == self.tail:
                    break
                temp = temp.next
            temp.next = self.head
            self.tail = temp
        else:
            index = 0
            temp = self.head
            while index < location - 1:
                index += 1
                temp = temp.next
            temp.next = temp.next.next

    def deleteEntireCSLL(self):
        if self.head is None:
            return
        self.head.next = None
        self.head = None
        self.tail = None


circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(2, -1)
circularSLL.insertCSLL(3, -1)
circularSLL.insertCSLL(4, -1)
circularSLL.insertCSLL(5, -1)
circularSLL.insertCSLL(0, -1)
circularSLL.insertCSLL(0, 0)
circularSLL.deleteNode(0)
circularSLL.deleteNode(-1)
circularSLL.deleteNode(2)
circularSLL.deleteEntireCSLL()

print([node.value for node in circularSLL])
