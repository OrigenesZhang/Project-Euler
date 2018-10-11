upp = 2000000
maxn = upp + 123
vis = [False for _i in range(maxn)]
primes = []

primes.append(2)
for i in range(3, upp, 2):
    if not vis[i]:
        primes.append(i)
    for j in primes:
        if i * j >= upp:
            break
        vis[i * j] = True
        if i % j == 0:
            break

print(sum(primes))
