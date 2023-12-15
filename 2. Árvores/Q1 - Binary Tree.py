class Node:
    def __init__(self, valor, nodeDir, nodeEsq):
        self.valor = valor
        self.direita = nodeDir
        self.esquerda = nodeEsq


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None


    def inserir(self, novoValor):
        novoNode = Node(novoValor, None, None)

        if self.raiz == None: #se a arvore for vazia
            self.raiz = novoNode

        else: #se já tiver uma raiz
            nodeAtual = self.raiz

            while True:
                nodeAnterior = nodeAtual
                if novoNode.valor <= nodeAtual.valor:                   #NOVO NODE *MENOR OU IGUAL* AO NODE ATUAL
                    nodeAtual = nodeAtual.esquerda
                    if nodeAtual == None:
                        nodeAnterior.esquerda = novoNode
                        return

                else:                                                   #NOVO NODE *MAIOR QUE* O NODE ATUAL
                    nodeAtual = nodeAtual.direita
                    if nodeAtual == None:
                        nodeAnterior.direita = novoNode
                        return

    def travessiaInOrder(self, atual, lista):                           #TRAVESSIA COM RECURSÃO
        if atual is not None:
            self.travessiaInOrder(atual.esquerda, lista)
            lista.append(atual.valor)
            self.travessiaInOrder(atual.direita, lista)

    def executarTravessia(self):
        listaInOrder = []
        self.travessiaInOrder(self.raiz, listaInOrder)
        print(' '.join(map(str, listaInOrder)))

arvore = ArvoreBinaria()
inputNodes = list(map(int, input().split(' '))) #Insira aqui os itens que quer adicionar na árvore

for i in inputNodes:
    arvore.inserir(i) #Inserindo os nós

output = arvore.executarTravessia()


