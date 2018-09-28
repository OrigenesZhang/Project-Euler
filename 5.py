def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a // gcd(a, b) * b

ans = 1
for i in range(1, 21):
    ans = lcm(ans, i)
print(ans)
