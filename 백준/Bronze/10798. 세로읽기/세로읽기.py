import sys

def vertical_reading(strings):
    max_length = max(len(s) for s in strings) 
    result = []

    for col in range(max_length):
        for row in range(5): 
            if col < len(strings[row]):  
                result.append(strings[row][col])

    return ''.join(result)

if __name__ == "__main__":
    strings = [sys.stdin.readline().strip() for _ in range(5)]

    print(vertical_reading(strings))