def ocorreRecursivo(texto, padrao):
    if len(texto) < len(padrao):
        return False
    
    if texto[:len(padrao)] == padrao:
        return True
    
    return ocorreRecursivo(texto[1:], padrao) 


print(ocorreRecursivo("hello world", "world"))  # Esperado: True
print(ocorreRecursivo("hello world", "python"))  # Esperado: False
print(ocorreRecursivo("abcabcabc", "abc"))  # Esperado: True
print(ocorreRecursivo("abcdef", "def"))  # Esperado: True
print(ocorreRecursivo("abcdef", "gh"))  # Esperado: False
