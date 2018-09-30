primes = [2, 3, 5, 7, 11, 13]
now = 15
while len(primes) < 10001:
    flag = True
    for it in primes:
        if now % it == 0:
            flag = False
            break
    if flag:
        primes.append(now)
    now += 2
print(primes[-1])
