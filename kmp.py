from typing import List


def kmp(s: str) -> List[int]:
    n = len(s)
    f = [0] * (n + 1)
    j = 0
    for i in range(1, n):
        while j and s[i] != s[j]:
            j = f[j]
        j += s[i] == s[j]
        f[i + 1] = j
    return f
