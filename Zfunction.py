def Zfunction(s: str) -> list:
    n = len(s)
    z = [n] + [0] * n
    j = 1
    for i in range(1, n):
        z[i] = max(0, min(j + z[j] - i, z[i - j]))
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > j + z[j]:
            j = i
    return z
