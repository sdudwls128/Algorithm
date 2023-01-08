position = list(input())

x = int(ord(position[0]) - ord('a') + 1)
y = int(position[1])

move_types = [(-2, -1), (-2, 1), (2, -1), (2, 1),
              (-1, -2), (-2, 2), (1, -2), (1, 2)]
count = len(move_types)

for move in move_types:
    nx = x + move[0]
    ny = y + move[1]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        count -= 1

print(count)
