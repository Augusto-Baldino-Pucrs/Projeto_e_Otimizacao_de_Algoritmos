import random
import time

def maxVal1(A, n):  
    max_value = A[0]
    interactions = 0
    for i in range(1, n): 
        interactions += 1
        if A[i] > max_value: 
           max_value = A[i]
    return max_value, interactions

def maxVal2(A, init, end, counter):
    counter["iterations"] += 1 
    
    if end - init <= 1:
        return max(A[init], A[end])
    else:
        m = (init + end) // 2
        v1 = maxVal2(A, init, m, counter)
        v2 = maxVal2(A, m + 1, end, counter)
        return max(v1, v2)

def testar_max_val():
    tamanhos = [32, 2048, 1048576]
    resultado = {}

    for n in tamanhos:
        RandomValue = [random.randint(1, 10000) for _ in range(n)]
        
        # Teste para maxVal1 (iterativo)
        start_time = time.perf_counter()
        max_value1, iteracoes1 = maxVal1(RandomValue, n)
        end_time = time.perf_counter()
        tempo_gasto1 = end_time - start_time

        # Teste para maxVal2 (Divisão e Conquista)
        counter = {"iterations": 0}  
        start_time = time.perf_counter()
        max_value2 = maxVal2(RandomValue, 0, n - 1, counter)
        end_time = time.perf_counter()
        tempo_gasto2 = end_time - start_time

        resultado[n] = {
            "Iterativo": {
                "Max Value": max_value1,
                "Iterações": iteracoes1,
                "Tempo Gasto (s)": tempo_gasto1
            },
            "Divisão e Conquista": {
                "Max Value": max_value2,
                "Iterações": counter["iterations"],
                "Tempo Gasto (s)": tempo_gasto2
            }
        }

    return resultado

resultados = testar_max_val()
for tamanho, dados in resultados.items():
    print(f"Vetor de tamanho {tamanho}:")
    print("  - Exercicío 2:")
    print(f"    - Máximo encontrado: {dados['Iterativo']['Max Value']}")
    print(f"    - Número de iterações: {dados['Iterativo']['Iterações']}")
    print(f"    - Tempo gasto: {dados['Iterativo']['Tempo Gasto (s)']:.6f} segundos")
    
    print("  - Exercicío 3:")
    print(f"    - Máximo encontrado: {dados['Divisão e Conquista']['Max Value']}")
    print(f"    - Número de iterações: {dados['Divisão e Conquista']['Iterações']}")
    print(f"    - Tempo gasto: {dados['Divisão e Conquista']['Tempo Gasto (s)']:.6f} segundos")
    
    print("-" * 50)
