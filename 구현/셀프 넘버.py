# 백준 4673
non_self = []

for i in range(1, 10001):
    non_self.append(i + sum(map(int, str(i))))

for i in range(1, 10001):
    if i not in non_self:
        print(i)
