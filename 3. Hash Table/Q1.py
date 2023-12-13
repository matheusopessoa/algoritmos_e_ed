class HashNode:
    def __init__(self, chave, valor):
        self.proximo = None
        self.chave = chave
        self.valor = valor

    def __str__(self):
        return f"Chave: {self.chave}, Valor: {self.valor}"


class HashTable:
    def __init__(self):
        self.table = [HashNode(i, 'vago') for i in range(0,10)]

    def __str__(self):
        return f'{[self.table[i].valor for i in range(0,10)]}'

    def add(self, node):
        chave = node.chave
        item = self.table[chave]

        while item.valor != 'vago':
            chave += 1
            if chave <= 9:
                item = self.table[chave]
            else:
                chave = -1

        self.table[chave] = node

class Grupos:
    def __init__(self, listaDiscipulos):
        self.listaDiscipulos = listaDiscipulos

    def dividir_grupos(self, lista_discipulos):
        grupos = []
        grupo_atual = []

        for discipulo in lista_discipulos:
            if discipulo not in grupo_atual:
                grupo_atual.append(discipulo)
            else:
                grupos.append(grupo_atual.copy())
                grupo_atual = [discipulo]

        if grupo_atual:
            grupos.append(grupo_atual.copy())

        return grupos

    def calcular_valor_grupo(self, grupo):
        return sum(ord(letra) for letra in grupo)

    def distribuir_grupos_dias(self, grupos):
        agenda = []

        for grupo in grupos:
            indexNodeAnterior = len(agenda) - 1 if len(agenda) > 0 else None

            valor_grupo = self.calcular_valor_grupo(grupo)
            dia = valor_grupo % 10

            grupoNode = HashNode(dia, grupo)
            agenda.append(grupoNode)

            if indexNodeAnterior:
                nodeAnt = agenda[indexNodeAnterior]
                nodeAnt.proximo = grupoNode

        return agenda

lista_discipulos = input('')
grupos_instance = Grupos(lista_discipulos)
resultado = grupos_instance.dividir_grupos(lista_discipulos)
if len(resultado) > 10:
    resultado = resultado[:10]
gruposNode = grupos_instance.distribuir_grupos_dias(resultado)

hashTable = HashTable()

for grupo in gruposNode:
    chave = grupo.chave
    hashTable.add(grupo)

print(hashTable)


