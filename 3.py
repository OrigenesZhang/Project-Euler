import math
n = 600851475143
last = -1
upp = int(math.sqrt(n) + 0.5)
for i in range(3, upp + 1, 2):
    if n % i == 0:
        last = i
        while n % i == 0:
            n //= i
        if n == 1:
            break
if n > 1:
    last = n
print(last)
