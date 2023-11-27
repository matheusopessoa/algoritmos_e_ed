class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self, data):
        current = self.head

        while current:
            if current.data == data:
                if current.prev_node:
                    current.prev_node.next_node = current.next_node
                else:
                    self.head = current.next_node

                if current.next_node:
                    current.next_node.prev_node = current.prev_node
                else:
                    self.tail = current.prev_node
                return
            current = current.next_node

    def display_backward(self):
        current = self.tail
        while current:
            if current.data is not None:
                print(current.data, end="\n")
            current = current.prev_node


    def search(self, data):
        current_node = self.head
        if current_node:
            while current_node is not None:
                if current_node.data == data:
                    return True
                current_node = current_node.next_node
        return False

    def interagiu(self, input):
        words = input.split(' ')
        action = words[1]
        name = words[-1]

        if action == 'deixou':
            self.remove(name)
        elif action == 'fechou':
            return
        else:
            if self.search(name) == False:
                self.append(name)
            else:
                self.remove(name)
                self.append(name)
fim = False
lista = DoublyLinkedList()
while (not fim):
    entradas = input()
    elemento = entradas[0]
    comando = entradas[-1]
    words = entradas.split(' ')
    if words[1] == 'fechou':
        fim = True
    lista.interagiu(entradas)
lista.display_backward()
