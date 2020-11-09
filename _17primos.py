import time


def sieve(n):
    ini = time.time()
    m = (n - 1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p * p < n:
        if b[i]:
            ps.append(p)
            j = 2 * i * i + 6 * i + 3
            while j < m:
                b[j] = False
                j = j + 2 * i + 3
        i += 1;
        p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1;
        p += 2
    fim = time.time()
    return ps


print(len(sieve(1000000)))  # 78498
print((fim - ini) / 60)