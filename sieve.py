minp, primes = [], []


def sieve(N: int) -> None:
    global minp, primes
    minp = [0] * (N + 1)
    primes = []

    for i in range(2, N + 1):
        if minp[i] == 0:
            minp[i] = i
            primes.append(i)

        for p in primes:
            if i * p > N:
                break

            minp[i * p] = p
            if p == minp[i]:
                break

    return
