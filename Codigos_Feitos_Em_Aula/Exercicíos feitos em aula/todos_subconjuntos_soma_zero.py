import time

def todos_subconjuntos_soma_zero(nums):
    resultados = []
    iteracoes = [0]  # Usamos uma lista para poder modificar dentro da função interna

    def backtrack(start, caminho, soma):
        iteracoes[0] += 1  # Conta cada chamada de backtrack
        if soma == 0 and caminho:
            print(f"Subconjunto encontrado: {caminho}")
            resultados.append(list(caminho))
        for i in range(start, len(nums)):
            backtrack(i + 1, caminho + [nums[i]], soma + nums[i])

    print(f"Conjunto fornecido: {nums}")
    inicio = time.time()
    backtrack(0, [], 0)
    fim = time.time()

    print(f"\nTotal de iterações (chamadas recursivas): {iteracoes[0]}")
    print(f"Total de subconjuntos encontrados: {len(resultados)}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")
    return resultados

# Teste com o exemplo
todos_subconjuntos_soma_zero([-7, 7, -2, -5, -8])
