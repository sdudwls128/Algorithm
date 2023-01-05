n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k != 0:
        count += n % k
        n -= n % k
    count += 1
    n //= k

print(count)
