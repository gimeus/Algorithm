import sys
input = sys.stdin.readline

def divide_and_conquer(x, y, size):
    global white, blue
    color = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                new_size = size // 2
                divide_and_conquer(x, y, new_size)
                divide_and_conquer(x, y + new_size, new_size)
                divide_and_conquer(x + new_size, y, new_size)
                divide_and_conquer(x + new_size, y + new_size, new_size)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0, 0
divide_and_conquer(0, 0, n)
print(white)
print(blue)