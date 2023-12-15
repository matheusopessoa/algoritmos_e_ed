class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.direita = None
        self.esquerda = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        item = Node(valor)

        if self.raiz == None:
            self.raiz = item

        else:
            adicionado = False
            itemAtual = self.raiz
            while not adicionado:
                if itemAtual.valor < item.valor:
                    if itemAtual.direita == None:
                        itemAtual.direita = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.direita
                else:
                    if itemAtual.esquerda == None:
                        itemAtual.esquerda = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.esquerda

    def buscaCulpado(self):
        if self.raiz is None:
            return None

        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda

        return atual.valor


numbers = list(map(int, input().split(' ')))

tree = Arvore()
for numero in numbers:
    tree.inserir(numero)

culpado = tree.buscaCulpado()
print(f"{culpado} puxou a camisa de {tree.raiz.valor}")
