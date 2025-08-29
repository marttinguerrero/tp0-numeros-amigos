import time

def amigos(MAX: int):

    t1 = time.time()
    if MAX < 2:
        print(0.0)
        return

    suma_divisores_propios = [0] * (MAX + 1)

    for d in range(1, MAX // 2 + 1):
        for m in range(2 * d, MAX + 1, d):
            suma_divisores_propios[m] += d

    for i in range(2, MAX + 1):
        s = suma_divisores_propios[i]
        if s > i and s <= MAX and suma_divisores_propios[s] == i:
            print(i, s)

    t2 = time.time()
    print(t2 - t1)


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    amigos(n)