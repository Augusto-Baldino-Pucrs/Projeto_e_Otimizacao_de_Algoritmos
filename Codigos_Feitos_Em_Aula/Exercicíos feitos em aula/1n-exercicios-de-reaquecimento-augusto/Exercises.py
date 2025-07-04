from itertools import permutations


# Multiplicação de dois números naturais, através de somas sucessivas (Ex.: 6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4).

def Recursive_Multiplication(n,m):
    if(m==0):
        return 0
    return n + Recursive_Multiplication(n,m-1)

print(Recursive_Multiplication(6, 4))  
print(Recursive_Multiplication(3, 5))  
print(Recursive_Multiplication(7, 0)) 

# Soma de dois números naturais, através de incrementos sucessivos (Ex.: 3 + 2 = + + (+ + + 1)).

def Recursive_Sum(n1, n2):
    if n2 == 0:  
        return n1
    return Recursive_Sum(n1 + 1, n2 - 1) 


print(Recursive_Sum(3, 2)) 
print(Recursive_Sum(0, 7))  
print(Recursive_Sum(10, 0)) 

# Cálculo de 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.

def Recursive_Sum_2(n,limit):
    if n > limit:
        return 0
    return 1/n + Recursive_Sum_2(n+1,limit)

print(Recursive_Sum_2(1, 4))   
print(Recursive_Sum_2(1, 10))  
print(Recursive_Sum_2(1, 1))   

# Inversão de uma string.

def reverse_string(s):
    if len(s) == 0: 
        return s
    return reverse_string(s[1:]) + s[0]  

print(reverse_string("augusto"))  
print(reverse_string("carro"))  

# Gerador da sequência dada por:
# F(1) = 1
# F(2) = 2
# F(n) = 2 ∗ F(n − 1) + 3 ∗ F(n − 2).

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 2 * F(n - 1) + 3 * F(n - 2)

print(F(1)) 
print(F(2))  
print(F(3)) 
print(F(4)) 
print(F(5)) 

# Gerador de Sequência de Ackerman:

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

print("Ackermann(2, 2):", ackermann(2, 2))

# A partir de um vetor de números inteiros, calcule a soma e o produto dos elementos do vetor.

def sum_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

print("Soma dos elementos [1, 2, 3, 4]:", sum_recursive([1, 2, 3, 4]))

def product_recursive(lst):
    if not lst:
        return 1
    return lst[0] * product_recursive(lst[1:])

print("Produto dos elementos [1, 2, 3, 4]:", product_recursive([1, 2, 3, 4]))


# Verifique se uma palavra é palíndromo (Ex. aba, abcba, xyzzyx).

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

print("'abcba' é palíndromo?", is_palindrome("abcba"))

# Dado um número n, gere todas as possíveis combinações com as n primeiras letras do alfabeto. Ex.: n = 3. Resposta: ABC, ACB, BAC, BCA, CAB, CBA.

def generate_combinations(n):
    letters = [chr(65 + i) for i in range(n)]
    return ["".join(p) for p in permutations(letters)]

print("Combinações para n=3:", generate_combinations(3))

# Defina uma sequência de Fibonacci generalizada, de f0 a f1 como sequência fibg(f0, f1, 0), fibg(f0, f1, 1), fibg(f0, f1, 2), ..., onde:
# fibg(f0, f1, 0) = f0
# fibg(f0, f1, 1) = f1
# fibg(f0, f1, n) = fibg(f0, f1, n − 1) + fibg(f0, f1, n − 2), se n > 1.

def generalized_fibonacci(f0, f1, n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    return generalized_fibonacci(f0, f1, n - 1) + generalized_fibonacci(f0, f1, n - 2)

print("Generalized Fibonacci(3, 5, 6):", generalized_fibonacci(3, 5, 6))


