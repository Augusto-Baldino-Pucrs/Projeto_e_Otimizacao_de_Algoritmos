def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    iterations = 0
    positions = []
    
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            iterations += 1
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    
    return positions, iterations

def horner_hash(s, d=256, q=101):
    h = 0
    for char in s:
        h = (h * d + ord(char)) % q
    return h

def rabin_karp_no_rolling(text, pattern):
    n, m = len(text), len(pattern)
    pattern_hash = horner_hash(pattern)
    positions = []
    iterations = 0

    for i in range(n - m + 1):
        substring = text[i:i + m]
        substring_hash = horner_hash(substring)
        iterations += m
        if substring_hash == pattern_hash:
            if substring == pattern:
                positions.append(i)

    return positions, iterations

def rabin_karp_rolling(text, pattern, d=256, q=101):
    n, m = len(text), len(pattern)
    h = pow(d, m - 1, q)
    pattern_hash = 0
    window_hash = 0
    iterations = 0
    positions = []

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        iterations += 1
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                positions.append(i)
        if i < n - m:
            window_hash = (d * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if window_hash < 0:
                window_hash += q

    return positions, iterations

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    iterations = 0
    positions = []

    while i < n:
        iterations += 1
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            positions.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions, iterations

text = "ababcabc"
pattern = "abc"

print("🔎 Testes com strings pequenas:")
for func in [naive_search, rabin_karp_no_rolling, rabin_karp_rolling, kmp_search]:
    result, iterations = func(text, pattern)
    print(f"{func.__name__:<25} -> Posições: {result}, Iterações: {iterations}")

print("\n🧪 Testes com string grande (>500.000 caracteres):")
import time

big_text = "a" * 500_000 + "b"
pattern = "a" * 100 + "b"

for func in [naive_search, rabin_karp_no_rolling, rabin_karp_rolling, kmp_search]:
    start = time.time()
    result, iterations = func(big_text, pattern)
    end = time.time()
    print(f"{func.__name__:<25} -> Posições: {result}, Iterações: {iterations}, Tempo: {end - start:.5f}s")

