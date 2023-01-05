coin_type = []
count = 0
n, k = map(int, input().split())
for _ in range(n):
    coin_type.append(int(input()))
for coin in reversed(coin_type):
    if k >= coin:
        count += k // coin
        k -= (k // coin) * coin
    if k == 0:
        break
print(count)
