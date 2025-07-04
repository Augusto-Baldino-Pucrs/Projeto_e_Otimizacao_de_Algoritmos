def merge_sort_rec(arr):

    # Implementação recursiva do Merge Sort.
    # Divide o array em partes menores, ordena e depois mescla

    if len(arr) <= 1:
        return arr #Caso base: Se houver um único elemento, já está ordenado
    
    # Passo 1: Dividir array ao meio
    meio = len(arr) // 2
    esquerda = merge_sort_rec(arr[:meio])
    direita = merge_sort_rec(arr[meio:])

    # Passo 2 e 3 conquistar e combinar ordenando subarrays

    return merge(esquerda, direita)

def merge(esquerda,direita):

    #Função auxiliar para mesclar dois arrays ordenados

    resultado = []
    i = j = 0

    #Percorre ambos os arrays ordenados e mescla-os na ordem correta

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i+= 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adiciona os elementos restantes (se houver)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

arr = [38, 27, 43, 3, 9, 82, 10]
print("Ordenado (Recursivo):", merge_sort_rec(arr))