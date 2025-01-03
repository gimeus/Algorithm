n = int(input())
times = list(map(int, input().split()))

times.sort()

total_time = 0
acc_time = 0

for time in times:
    acc_time += time
    total_time += acc_time

print(total_time)