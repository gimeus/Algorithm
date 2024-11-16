a, b = map(int, input().split()) 

box = [i for i in range(1, a + 1)] 
for _ in range(b):
    i, j = map(int, input().split())
    box[i - 1], box[j - 1] = box[j - 1], box[i - 1]
    
print(" ".join(map(str, box)))