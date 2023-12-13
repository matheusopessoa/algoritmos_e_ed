class Node:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = {}

    def adicionar_pessoa(self, nome, tamanho_grupo):
        if tamanho_grupo not in self.tabela:
            self.tabela[tamanho_grupo] = Node(nome)
        else:
            no = Node(nome)
            atual = self.tabela[tamanho_grupo]

            if nome < atual.nome:
                no.proximo = atual
                self.tabela[tamanho_grupo] = no
            else:
                while atual.proximo and nome > atual.proximo.nome:
                    atual = atual.proximo
                no.proximo = atual.proximo
                atual.proximo = no

    def obter_grupos(self):
        resultado = []
        for tamanho_grupo in sorted(self.tabela.keys()):
            atual = self.tabela[tamanho_grupo]
            while atual:
                grupo = [atual.nome]
                for _ in range(tamanho_grupo - 1):
                    if atual.proximo:
                        atual = atual.proximo
                        grupo.append(atual.nome)
                resultado.append(grupo)
                if atual.proximo:
                    atual = atual.proximo
                else:
                    break
        return resultado

def formar_grupos():
    linhas_entrada = []
    while True:
        try:
            linha = input().strip()
            if not linha:
                break
            linhas_entrada.append(linha)
        except EOFError:
            break

    tabela_hash = TabelaHash()

    for linha in linhas_entrada:
        nome, tamanho_grupo = linha.split()
        tamanho_grupo = int(tamanho_grupo)
        tabela_hash.adicionar_pessoa(nome, tamanho_grupo)

    grupos = tabela_hash.obter_grupos()
    return grupos

saida = formar_grupos()
print(saida)
