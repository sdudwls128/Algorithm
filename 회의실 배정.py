# 백준 1931번
# 회의 시작 시간을 기준으로 한 번 정렬하고 끝나는 시간을 기준으로 다시 정렬하면 가장 적은 회의시간을 가진 순서로 정렬된다.
n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings = sorted(meetings, key=lambda a: a[0])
meetings = sorted(meetings, key=lambda a: a[1])
result = 0
last = 0

for start_time, end_time in meetings:
    if start_time >= last:
        result += 1
        last = end_time

print(result)


# !! 시간초과
# n = int(input())
# meetings = [list(map(int, input().split())) for _ in range(n)]
# meetings.sort()
# count = 0
# result = 0
# end_time = 0

# for i in range(n):
#     count = 1
#     end_time = meetings[i][1]

#     for j in range(i+1, n):
#         if meetings[j][0] >= end_time:
#             end_time = meetings[j][1]
#             count += 1
#     result = max(count, result)

# print(result)
