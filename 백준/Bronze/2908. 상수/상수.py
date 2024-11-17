num1, num2 = input().split()

reversed_num1 = int(num1[::-1])
reversed_num2 = int(num2[::-1])

print(max(reversed_num1, reversed_num2))