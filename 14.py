mem = {}
mem[1] = 1

def dfs(u):
    if u in mem:    
        return mem[u]
    if u % 2 == 0:
        mem[u] = dfs(u // 2) + 1
    else:
        mem[u] = dfs(3 * u + 1) + 1
    return mem[u]

ans = 1
for i in range(1, 1000000):
    if dfs(i) > dfs(ans):
        ans = i
print(ans)

