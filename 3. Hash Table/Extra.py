def ajustar_heap(arr, tamanho, i):
    maior = i
    esquerda, direita = 2 * i + 1, 2 * i + 2

    maior = esquerda if esquerda < tamanho and arr[i] < arr[esquerda] else maior
    maior = direita if direita < tamanho and arr[maior] < arr[direita] else maior

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        ajustar_heap(arr, tamanho, maior)

def heapsort(arr):
    tamanho = len(arr)

    for i in range(tamanho // 2 - 1, -1, -1):
        ajustar_heap(arr, tamanho, i)

    for i in range(tamanho - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        ajustar_heap(arr, i, 0)

def calcular_multiplicacao_maxima(arr):
    heapsort(arr)
    return arr[-1] * arr[-2]


numeros = list(map(int, input('').split(',')))


if len(numeros) < 2:
    print('')
else:
    resultado = calcular_multiplicacao_maxima(numeros)
    print("R$" + str(resultado))
