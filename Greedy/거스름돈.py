# 거슬러줘야 할 돈 n을 입력받고 거슬러줘야 하는 동전의 개수를 구하는 문제
# 처음에 str 연산 오류가 났다. 오류 원인: 입력값의 유형을 정수로 지정하지 않았기 때문
n = int(input())
count = 0
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    print(count)
    if n == 0:
        break
