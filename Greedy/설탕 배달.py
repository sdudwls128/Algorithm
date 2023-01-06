# 백준 2839번
n = int(input())
count = 0
while n > 0:
    if n % 5 != 0:
        count += 1
        n -= 3
    else:
        count += 1
        n -= 5
print(count if n == 0 else -1)
