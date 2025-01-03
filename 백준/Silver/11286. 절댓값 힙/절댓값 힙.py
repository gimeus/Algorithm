import sys
import heapq

input = sys.stdin.readline

n = int(input())
abs_heap = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(x), x))