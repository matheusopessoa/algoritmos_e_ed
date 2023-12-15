#essa questão foi surpresa, feita em sala e com tempo limite.
#basicamente, deveriamos fazer uma pilha, foi bem simples.

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        newNode = Node(data)
        newNode.next_node = self.top
        self.top = newNode

    def pop(self):
        if not self.is_empty():
            poppedData = self.top.data
            self.top = self.top.next_node
            return poppedData
        else:
            return None

    def get(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next_node
        return elements


def main():
    stack = Stack()

    elements = input()

    for element in elements.split():
        stack.push(element)

    print(f"Pilha: {stack.get()}")

    for _ in range(len(elements.split())):
        popped_element = stack.pop()
        print(f"Removido: {popped_element}")
        print(f"Pilha: {stack.get()}")

if __name__ == "__main__":
    main()