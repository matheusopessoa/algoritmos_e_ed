class Node:
    def __init__(self, nome, tamanho_grupo):
        self.nome = nome
        self.tamanho_grupo = tamanho_grupo
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.inicio = None

    def adicionar_pessoa(self, nome, tamanho_grupo):
        novo_no = Node(nome, tamanho_grupo)

        if not self.inicio:
            self.inicio = novo_no
            return

        atual = self.inicio
        anterior = None

        while atual and (tamanho_grupo > atual.tamanho_grupo or (tamanho_grupo == atual.tamanho_grupo and nome >= atual.nome)):
            anterior = atual
            atual = atual.proximo

        if not anterior:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            anterior.proximo = novo_no
            novo_no.proximo = atual

    def obter_grupos(self):
        resultado = []
        atual = self.inicio

        while atual:
            grupo = [atual.nome]
            for _ in range(atual.tamanho_grupo - 1):
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
        tabela_hash.adicionar_pessoa(nome, int(tamanho_grupo))

    grupos = tabela_hash.obter_grupos()
    return grupos

saida = formar_grupos()
print(saida)
