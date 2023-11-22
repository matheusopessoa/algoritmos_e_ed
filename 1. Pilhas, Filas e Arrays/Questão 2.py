class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None #primeiro nó (referencia)

    def append(self, element):
        if self.head:
            pointer = self.head
            while(pointer.nextNode):
                pointer = pointer.nextNode
            pointer.nextNode = Node(element)
        else:
            self.head = Node(element)

    def remove(self, element):
        if self.head.data == element:
            self.head = self.head.nextNode
        else:
            pointer = self.head
            while(pointer.nextNode is not None): #quando removermos ele virará None
                if pointer.data == element:
                    pointer.nextNode = pointer.nextNode.nextNode
                    break
                pointer = pointer.nextNode
            return 'Node {element} não existe'
    
    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.nextNode
            i = i+1

    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.nextNode
        return r

    def empurrar(self, element):
        pointer = self.head
        if pointer.data == element:
            if pointer.nextNode.nextNode is not None:
                segundo = pointer.nextNode
                terceiro = pointer.nextNode.nextNode
                saveData.nextNode = segundo
                pointer.nextNode = terceiro
                segundo.nextNode = pointer
                
            

listaa = LinkedList()
fim = False

while(not fim):
    entradas = input().split(':')
    elemento = entradas[0]
    comando = entradas[-1]
    if comando == 're':
        listaa.remove(elemento)

    elif comando == 'add':
        listaa.append(elemento)

    elif comando == 'em':
        listaa.empurrar(elemento)


    elif comando == 'fim!':
        fim = True
        break

    elif comando == 'pri':
        print(listaa.__repr__)


