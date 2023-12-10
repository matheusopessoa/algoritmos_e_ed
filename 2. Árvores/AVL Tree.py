class AVLNode:
    def __init__(self):
        self.pai = None
        self.esquerda = None
        self.direita = None
        self.altura = 0
        self.valor

    def check_filhos(self):
        #return dois_filhos, apenas_esq, apenas_dir, isLeaf

        if self.esquerda and self.direita: #se tiver os 2 filhos
            return True, False, False, False
        
        elif self.direita and not self.esquerda: #apenas filho na direta
            return False, False, True, False
        
        elif self. esquerda and not self.direita: #apenas filho na esquerda
            return False, True, False, False
        else:
            return False, False, False, True #é uma folha
    
    def altura_maxima_filho(self, node):
        doisFilhos, apenasEsquerda, apenasDireita, folha = node.check_filhos

        if doisFilhos: #se tiver os 2 filhos
            return max(self.esquerda.altura, self.direita.altura)
        
        elif apenasDireita: #apenas filho na direta
            return self.direita.altura
        
        elif apenasEsquerda: #apenas filho na esquerda
            return self.direita.altura
        
        elif folha:
            return -1
        
    def fator_de_balanceamento(self):
        return (self.esquerda.altura if self.esquerda else -1) - (self.direita.altura if self.direta else -1)
    
    def __str__(self): #Para ficar mais facil identificar o node printando apenas ele
        return "Node da AVL: \n" + "Valor: " + str(self.valor) + "\nAltura: " + str(self.altura)
    

class AVLTree:
    def __init__(self):
        self.raiz = None
        self.total_nodes = 0

    def inserir(self, valor):
        if not self.raiz: #arvore vazia
            self.raiz = AVLNode(valor)
        else:
            self._inserir(self, self.raiz, valor)
        self.total_nodes += 1

    def _inserir(self, raiz, valor):

        if raiz.valor < valor: #IR PRA DIREITA
            if raiz.direita:
                self._inserir(self, raiz.direita, valor)
            else:
                novo_filho = AVLNode(valor)
                raiz.direita = novo_filho
                novo_filho.pai = raiz
                total_nodes += 1
                #Node adicionado, agora devemos balancear a tree
                
                #Por questão de otimizaçao, só é necessário atualizar as alturas se a altura do
                #node atual for = 0 ''
                #if raiz.altura == 0:
                #    self.att_alturas(self, novo_filho)
                #    while raiz:
                #        if raiz.fator_de_balanceamento() in [2, -2]:


        
        else: #IR PARA ESQUERDA 
            if raiz.esquerda:
                self._inserir(self, raiz.esquerda, valor)
            else:
                novo_filho = AVLNode(valor)
                raiz.esquerda = novo_filho
                novo_filho.pai = raiz
                total_nodes += 1
                #TODO: if raiz.altura == 0:
                 
    def att_alturas(self, node_inicial):
        mudouAltura = False
        node = node_inicial
        while node and not mudouAltura:
            altura_anterior = node.altura
            node.height = (node.altura_maxima_filho() + 1)
            mudouAltura = not (altura_anterior == node.height)
            node = node.pai

    def rotacao_esq(self, node):
        a = node
        if a == self.raiz: 
                                           #a
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
            b.pai = d

    def rotacao_dir(self, node):
        a = node
        if a == self.raiz:

            b = a.esquerda 
            a.pai = b
            b.direita = a
            b.pai = None
        
        else:
            b = a.esquerda
            d = a.pai

            b.direia = a
            d.esquerda = b

            b.pai = d
            a.pai = b



    

       