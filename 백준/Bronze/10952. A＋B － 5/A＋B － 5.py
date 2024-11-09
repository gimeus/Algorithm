import sys

for line in sys.stdin:
    A, B = map(int, line.split())
    
    if A == 0 and B == 0:
        break
    
    print(A + B)
