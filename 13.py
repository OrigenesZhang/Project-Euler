f = open('13.in', 'r')
ans = 0
for i in range(100):
    now = int(f.readline())
    ans += now
ans = str(ans)
print(ans[:10])

