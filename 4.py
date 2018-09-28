ans = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        now = str(i * j)
        for pos in range(len(now) // 2):
            if now[pos] != now[-pos - 1]:
                now = None
                break
        if now is not None:
            ans = max(ans, int(now))
print(ans)
