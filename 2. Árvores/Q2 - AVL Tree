class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0


class AVL(object):
    def __init__(self):
        self.root = None


    def calcHeight(self,node):
        if not node:
            return -1
        return node.height


    def insert(self, data):
        self.root = self.insertNode(data, self.root)


    def insertNode(self, data, node):
        if not node:
            return Node(data)
        else:
            if data < node.data:
                node.leftChild = self.insertNode(data, node.leftChild)
            else:
                node.rightChild = self.insertNode(data, node.rightChild)

        return self.settleViolation(data, node)


    def settleViolation(self, data, node):
        balance = self.calcBalance(node)

        if balance > 1 and data < node.leftChild.data:
            return self.rotateRight(node)

        if balance < -1 and data > node.rightChild.data:
            return self.rotateLeft(node)

        if balance > 1 and data > node.leftChild.data:
            node.leftChild = self.rotateLeft(node.leftChild, data)
            return self.rotateRight(node)

        if balance < -1 and data < node.rightChild.data:
            node.rightChild = self.rotateRight(node.rightChild, data)
            return self.rotateLeft(node)
        return node


    def calcBalance(self,node):
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)


    def rotateRight(self,node, newdata=0):
        if node.leftChild == None: #evita bugs do tipo (x x x x...) insert(y) com x>y
            node.leftChild = Node(newdata)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1
        return tempLeftChild


    def rotateLeft(self,node):
        a = node
        if node == self.raiz:              #a
            b = a.direita                    #b
            b.esquerda = node                  #c
            a.pai = b
            b.pai = None
         
        else:                               
            d = a.pai            
            b = a.direita

            d.direita = b
            b.esquerda = a
            a.pai = b
            b. pai = d
        return b    


    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node


    def traverse(self):
        listaIn = []
        if self.root:
            self.traverseInOrder(self.root, listaIn)
        return listaIn


    def traverseInOrder(self, node, lista):
        if node.leftChild:
            self.traverseInOrder(node.leftChild, lista)
        lista.append(node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild, lista)

qtdAulasPorEscola = input().split(' ')
qtdAulasHog = int(qtdAulasPorEscola[0])
qtdAulasCIn = int(qtdAulasPorEscola[1])
avl = AVL()


if qtdAulasHog > 0:
    conhecimentoHOG = list(map(int, input().split(' '))) #Insira aqui os itens que quer adicionar na árvore
    for i in conhecimentoHOG:
        if len(conhecimentoHOG) < 50:
            avl.insert(i)  # Inserindo os nós Hog
else:
    inputInevital = input()

if qtdAulasCIn > 0:
    conhecimentoCIn = list(map(int, input().split(' '))) #Insira aqui os itens que quer adicionar na árvore
    for i in conhecimentoCIn:
        if 1 <= i <= 50:
            if len(conhecimentoCIn) < 50:
                avl.insert(i)
else:
    inputInevital = input()

k = int(input()) #qtsAulasVer

if qtdAulasCIn > 0 or qtdAulasHog > 0:
    listaInOrder = avl.traverse()
    qtdTotalAulas = len(listaInOrder)

    if 0 < k <= qtdTotalAulas:
        if k>40:
            k=40
            print(f'valor total de conhecimento: {sum(listaInOrder[(-k):])}')
        else:
            print(f'valor total de conhecimento: {sum(listaInOrder[(-k):])}')
    elif k > qtdTotalAulas:
        print(f'valor total de conhecimento: {sum(listaInOrder)}')

else:
    print('valor total de conhecimento: 0')


