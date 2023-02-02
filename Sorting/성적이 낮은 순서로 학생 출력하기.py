n = int(input())
arr = {}
for i in range(n):
    data = input().split()
    arr[data[0]] = int(data[1])

arr = sorted(arr.items(), key=lambda x: x[1])

for s in arr:
    print(s[0], end=' ')
