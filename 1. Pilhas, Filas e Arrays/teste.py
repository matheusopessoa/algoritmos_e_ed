class Node:
    def __init__(self, data, prev_node, next_node):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class DoublyLinkedList:
    head = None
    tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node

    def remove(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev_node is None:
                    self.head = current_node.next_node
                    if current_node.next_node is not None:
                        current_node.next_node.prev_node = None
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    if current_node.next_node is not None:
                        current_node.next_node.prev_node = current_node.prev_node
            current_node = current_node.next_node

    def display(self):
        current_node = self.head
        nodes = []
        while current_node is not None:
            current_data = str(current_node.data)
            nodes.append(current_data)
            current_node = current_node.next_node

        while len(nodes) > 1:
            print(nodes[-1])
            nodes.remove(nodes[-1])

        return nodes[0]
    

lista = DoublyLinkedList()

fim = False

while(not fim):
    entradas = input().split(':')
    elemento = entradas[0]
    comando = entradas[-1]
    if comando == 're':
        print(lista.remove(elemento))

    elif comando == 'add':
        print(lista.append(elemento))

    elif comando == 'fi':
        fim = True
        print(lista.display())
        break
