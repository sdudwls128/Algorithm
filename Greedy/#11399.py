n = int(input())
arr = list(map(int, input().split()))
time = 0
arr.sort(reverse=True)
for i in range(n):
    time += arr[i] * (i + 1)
print(time)
