# Problem Statement

# Para a organização de uma pilha de materiais em um vestiário do campeonato mundial de 1x1 FIFA. você ficou responsável em conferir se cada camisa com o nome de jogador vai receber sua chuteira da marca que representa. Levando em conta que 4 jogadores renomados: Endrick, Neymar, CR7 e Messi estarão nesse campeonato e representam marcas específicas - "new balance", "puma", "nike" e "adidas", respectivamente. Organize a pilha de materiais para que cada camisa (representada pelo nome do jogador) fique seguido da chuteira (representada pela marca).

# Regra geral: Toda camisa precisa ter a chuteira depois dela, não necessariamente imediatamente após, mas eventualmente. Nenhuma chuteira pode aparecer sem que uma camisa tenha o antecedido em algum momento. E, atenção, uma pilha que tem a mesma quantidade de camisas e chuteiras NÃO está necessariamente correta.

# Proibido uso de bibliotecas
# Input

# A única linha de entrada é composta por uma string, que corresponde a pilha de camisas e chuteiras. A string é uma sequência de nomes e marcas com u hífen separando elas.

# Exemplo: "endrick-new balance-messi-adidas-cr7-messi-nike-endrick".

# Output

# Você deve produzir uma única linha de saída com a expressão “Correto.” caso a pilha seja bem formada, e “Incorreto” caso contrário.

def pilhaChecker(entrada):
    pilha = []
    camisas_chuteiras = entrada.split('-')

    for item in camisas_chuteiras:
        #varifico se é uma chave do dicionario (se for, é uma camisa/jogador (empilhar))
        if item in playersDict:
            pilha.append(item)
        #caso n seja uma chave, pode ser um valor... (chuteira)
        elif item in set(playersDict.values()): #a partir daqui, item=chuteira ou elemento invalido.
            #"a pilha está vazia OU não corresponde à camisa?" 
            if not pilha or playersDict[pilha.pop()] != item:
                return "Incorreto"
        else:
            #nesse caso, a entrada foi incorreta
            return "Incorreto"

    #se a pilha estiver vazia, significa que deu certo.
    return "Correto" if not pilha else "Incorreto"

playersDict = {"endrick": "new balance",
               "messi": "adidas",
               "cr7": "nike",
               "neymar": "puma"}

entrada = input()

resultado = pilhaChecker(entrada)
print(resultado)




    