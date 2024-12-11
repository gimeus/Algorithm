n = int(input()) 
divisors = list(map(int, input().split())) 
original_number = min(divisors) * max(divisors)

print(original_number)