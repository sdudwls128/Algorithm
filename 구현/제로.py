# 백준 10773번
n = int(input())
m = []

for i in range(n):
    data = int(input())
    if data == 0:
        m.pop()
        continue
    m.append(data)

print(sum(m))
