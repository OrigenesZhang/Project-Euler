upp = 4000000
ans = 2
a = 1
b = 2
while a + b <= upp:
    a, b = b, a + b
    if b % 2 == 0:
        ans += b
print(ans)
