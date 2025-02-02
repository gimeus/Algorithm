import sys
sys.setrecursionlimit(10**6)

def dfs(cur, parent):
    for next_node in graph[cur]:
        if next_node != parent:
            dfs(next_node, cur)
            dp[cur][1] += dp[next_node][0]  
            dp[cur][0] += max(dp[next_node][0], dp[next_node][1])

n = int(sys.stdin.readline())
population = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, population[i]] for i in range(n+1)]

dfs(1, -1)
print(max(dp[1][0], dp[1][1]))