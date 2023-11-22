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
        return f'Node {element} adicionado'

    def remove(self, element):
        if self.head == None:
            return f'Node {element} não existe' 

        elif self.head.data == element:
            self.head = self.head.nextNode
            return f'Node {element} foi removido'
    
        else:
            antecessor = self.head
            pointer = self.head.nextNode
            while(pointer):
                if pointer.data == element:
                    antecessor.nextNode = pointer.nextNode
                    pointer.nextNode = None                
                    return f'Node {element} foi removido'
                antecessor = pointer
                pointer = pointer.nextNode
            return f'Node {element} não existe'


    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.nextNode
        mapa = f'mapa:{r[:-2]}'
        return mapa


    def empurrar(self, element):
        pointer = self.head
        if pointer is not None:
            if pointer.nextNode is not None and pointer.data == element:
                segundo = pointer.nextNode
                pointer.data = segundo.data
                segundo.data = element
                return f'Node {element} empurrado'
            else:
                while(pointer.data is not element and pointer.nextNode is not None):
                    pointer = pointer.nextNode
                if pointer.nextNode is not None and pointer.data == element:
                    segundo = pointer.nextNode 
                    pointer.data = segundo.data
                    segundo.data = element
                    return f'Node {element} empurrado'
                elif pointer.nextNode is None and pointer.data == element:
                    return f'Não existe Node depois de {element}'
            return f'Node {element} não existe'
        else:
            return f'Node {element} não existe'
            
    def voltar(self, element):
        pointer = self.head
        if pointer is not None:
            if pointer.data == element:
                return f'Não existe node antes de {pointer.data}'
            else:
                antecessor = pointer
                pointer = pointer.nextNode
                while(pointer.data is not element and pointer.nextNode is not None):
                    antecessor = pointer
                    pointer = pointer.nextNode
                if pointer.data == element:
                    pointer.data = antecessor.data
                    antecessor.data = element
                    return f'Node {element} puxado'
                return f'Node {element} não existe'
        else:
            return f'Node {element} não existe'

lista = LinkedList()
fim = False

while(not fim):
    entradas = input().split(':')
    elemento = entradas[0]
    comando = entradas[-1]
    if comando == 'remova-me!' or comando == 're':
        print(lista.remove(elemento))

    elif comando == 'adicione-me!' or comando == 'add':
        print(lista.append(elemento))
        
    elif comando == 'empurre-me!' or comando == 'em':
        print(lista.empurrar(elemento))

    elif comando == 'puxe-me!' or comando == 'vol':
        print(lista.voltar(elemento))

    elif comando == 'fim!':
        fim = True
        print(repr(lista))
        break

    elif comando == 'pri':
        print(repr(lista))