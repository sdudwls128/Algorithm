# 백준 1316번

n = int(input())
count = n

for i in range(n):
    word = input()
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            count -= 1
            break

print(count)


# n = int(input())
# words = [list(input()) for _ in range(n)]
# count = 0

# for i in range(n):
#     tmp = []
#     is_group = 1
#     for j in words[i]:
#         if j not in tmp or j == tmp.pop():
#             tmp.append(j)
#         else:
#             is_group = 0
#             break
#     count += is_group

# print(count)
