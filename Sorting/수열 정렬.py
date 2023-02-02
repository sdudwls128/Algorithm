# 백준 1015번
n = int(input())
a = list(map(int, input().split()))
p = [0] * n

for i in range(n):
    index = a.index(min(a))
    p[index] = i
    a[index] = 1000

print(*p)

# n = int(input())
# t = list(map(int, input().split()))
# s_li = sorted(t)
# li = []
# for i in range(n):
#     idx = s_li.index(t[i])
#     li.append(idx)
#     s_li[idx] = -1
# print(*li)
