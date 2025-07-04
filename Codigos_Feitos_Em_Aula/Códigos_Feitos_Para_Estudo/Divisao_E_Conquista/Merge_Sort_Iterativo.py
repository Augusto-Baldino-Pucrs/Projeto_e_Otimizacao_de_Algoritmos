def merge_sort_iter(arr):
    # Implementação iterativa do Merge Sort.Utiliza um loop para dividir e mesclar os elementos progessivamente.

    if len(arr) <= 1:
        return arr 
    
#Inicialmente, cada lemento é considerado um array unitário 