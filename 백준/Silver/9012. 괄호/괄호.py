t = int(input())

for _ in range(t):
    ps = input().strip()
    stack = []
    is_valid = True

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break

    if is_valid and not stack:
        print("YES")
    else:
        print("NO")