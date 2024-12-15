import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

result = [binary_search(cards, target) for target in targets]
print(" ".join(map(str, result)))