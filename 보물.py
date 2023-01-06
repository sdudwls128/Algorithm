# 백준 1026번
# 너무 복잡하게 생각함. 그냥 a의 제일 작은 수와 b의 제일 큰 수를 곱하면 됨
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_copy = b[:]
a.sort()
b_copy.sort(reverse=True)

result = 0
for i in range(n):
    result += a[i] * b_copy[i]

print(result)
