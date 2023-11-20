class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n01 = Node(15)
n02 = Node(12)
n03 = Node(30)

class LinkedList:
    def __init__(self):
        self.head = None #primeiro nó (referencia)
        self.size = 0 

    def append(self, element):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            self.head = Node(element)
        self.size += 1

lista = LinkedList()

