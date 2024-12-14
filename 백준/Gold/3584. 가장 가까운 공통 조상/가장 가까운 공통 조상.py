import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def find_lca(node1, node2, parent, depth):
    while depth[node1] > depth[node2]:
        node1 = parent[node1]
    while depth[node2] > depth[node1]:
        node2 = parent[node2]
    
    while node1 != node2:
        node1 = parent[node1]
        node2 = parent[node2]
    
    return node1

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())  
        parent = [0] * (N + 1)
        depth = [0] * (N + 1)
        tree = defaultdict(list)
        
        for _ in range(N - 1):
            u, v = map(int, input().split())
            tree[u].append(v)
            parent[v] = u
        
        root = 1
        for i in range(1, N + 1):
            if parent[i] == 0:  
                root = i
                break
                
        queue = deque([root])
        depth[root] = 0
        while queue:
            current = queue.popleft()
            for child in tree[current]:
                depth[child] = depth[current] + 1
                queue.append(child)
        
        a, b = map(int, input().split())
        print(find_lca(a, b, parent, depth))

solve()