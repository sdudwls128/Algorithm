# 백준 1059번
l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()

if n in s:
    print(0)
else:
    for i in range(l-1):
        if s[i] < n and n < s[i+1]:
            print((n - s[i]) * (s[i+1] - n) - 1)
            break
