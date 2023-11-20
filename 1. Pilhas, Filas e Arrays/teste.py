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
