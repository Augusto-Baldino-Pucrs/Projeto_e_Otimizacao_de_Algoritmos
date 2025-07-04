def somaArray(lista):
    if not lista: 
        return 0
    return lista[0] + somaArray(lista[1:])  

print(somaArray([10, 92, 23, 54, 55]))  # Esperado: 15
