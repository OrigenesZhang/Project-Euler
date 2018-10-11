ans = 1
for i in range(20):
    ans *= 40 - i
for i in range(1, 21):
    ans //= i
print(ans)

