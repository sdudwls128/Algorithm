# 백준 1026번
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for i in range(n):
    result += max(a) * min(b)
    a[a.index(max(a))] = 0
    b[b.index(min(b))] = 101

print(result)
