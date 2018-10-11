import math
def cnt(n):
    upp = int(math.sqrt(n) + 0.5)
    ret = 0
    for i in range(1, upp + 1):
        if n % i == 0:
            if n // i == i:
                ret += 1
            else:
                ret += 2
    return ret

for n in range(1, 50000):
    now = n * (n + 1) // 2
    if cnt(now) > 500:
        print(now)
        break

