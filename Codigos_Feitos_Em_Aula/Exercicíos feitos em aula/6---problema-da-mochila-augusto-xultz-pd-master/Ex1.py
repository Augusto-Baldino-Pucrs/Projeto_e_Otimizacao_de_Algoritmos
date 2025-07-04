def FIBO_REC(n):
   if n <= 1:
    return n
   else:
    a = FIBO_REC(n - 1)
    b = FIBO_REC(n - 2)
    return a+b

print("FIBO_REC")
print(FIBO_REC(4))
print(FIBO_REC(8))  
print(FIBO_REC(16))  
print(FIBO_REC(32))

def FIBO(n):
    f = [0] * (n+1)
    f[0] = 0
    if n>0:
       f[1] = 1
       for i in range(2,n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

print("FIBO")
print(FIBO(4))
print(FIBO(8))  
print(FIBO(16))  
print(FIBO(32))
print(FIBO(128))  
print(FIBO(1000))  
print(FIBO(10000))
def lookup_fibo(f, n):
    if f[n] >= 0:
        return f[n]
    if n <= 1:
        f[n] = n
    else:
        f[n] = lookup_fibo(f, n - 1) + lookup_fibo(f, n - 2)
    return f[n]

def memorized_fibo(n):
    f = [-1] * (n + 1)
    return lookup_fibo(f, n)

print("memorized_fibo")
print(memorized_fibo(4))
print(memorized_fibo(8))  
print(memorized_fibo(16))  
print(memorized_fibo(32))
print(memorized_fibo(128))  
print(memorized_fibo(1000))  
print(memorized_fibo(10000))

