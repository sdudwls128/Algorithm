# 크기 n의 배열의 값을 m번 더해 최대값을 구함
# 같은 수는 연속해서 k번 더할 수 있음
# 느낀 점: 필요 없는 변수는 만들지 말고 여러 번 사용하거나 배열에 접근해야 하는 것들은 변수로 잘 만들어 사용하자
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

first, second = arr[0], arr[1]
result = 0

# while m != 0:
#     for _ in range(0, k):
#         result += first
#         m -= 1
#     result += second
#     m -= 1

# print(result)

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = count * first
result += (m - count) * second
