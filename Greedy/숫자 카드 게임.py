n, m = map(int, input().split())
result = 0

for i in range(n):
    cards = list(map(int, input().split()))
    min_value = min(cards)
    result = max(result, min_value)

print(result)
