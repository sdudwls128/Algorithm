# 백준 1966번
cases = int(input())

for i in range(cases):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    count = 0

    while m >= 0:
        if queue[0] == max(queue):
            m -= 1
            queue.pop(0)
            count += 1
        else:
            queue.append(queue[0])
            queue.pop(0)
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1
    print(count)
