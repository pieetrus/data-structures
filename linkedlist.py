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
    #insert in SLL

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
