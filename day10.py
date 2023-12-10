from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
start = None
g = []
for i, s in enumerate(s_list):
    g.append([])
    for j in range(len(s)):
        if s[j] == 'S':
            start = (i, j)
        g[i].append(s[j])

adj = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

cur = start[0], start[1]
cur2 = start[0], start[1]
cur3 = 0
prev = cur
prev2 = cur2
loop = [start]

# find two routes away from start

if start[0] + adj["up"][0] >= 0 and g[start[0] + adj["up"][0]][start[1] + adj["up"][1]] in "7|F":
    cur = start[0] + adj["up"][0], start[1] + adj["up"][1]
    cur3 = 1
if start[1] + adj["left"][1] >= 0 and g[start[0] + adj["left"][0]][start[1] + adj["left"][1]] in "L-F":
    if cur3 == 0:
        cur = start[0] + adj["left"][0], start[1] + adj["left"][1]
        cur3 = 1
    else:
        cur2 = start[0] + adj["left"][0], start[1] + adj["left"][1]
if start[0] + adj["down"][0] < len(g) and g[start[0] + adj["down"][0]][start[1] + adj["down"][1]] in "L|J":
    if cur3 == 0:
        cur = start[0] + adj["down"][0], start[1] + adj["down"][1]
        cur3 = 1
    else:
        cur2 = start[0] + adj["down"][0], start[1] + adj["down"][1]
if start[1] + adj["right"][1] < len(g[0]) and g[start[0] + adj["right"][0]][start[1] + adj["right"][1]] in "7-J":
    cur2 = start[0] + adj["right"][0], start[1] + adj["right"][1]

out += 1


def next_pipe(cur, prev):
    if prev == (cur[0] + 1, cur[1]):  # up
        if g[cur[0]][cur[1]] == "F":
            prev = cur
            cur = cur[0], cur[1] + 1
        elif g[cur[0]][cur[1]] == "7":
            prev = cur
            cur = cur[0], cur[1] - 1
        else:
            prev = cur
            cur = cur[0] - 1, cur[1]

    elif prev == (cur[0] - 1, cur[1]):  # down
        if g[cur[0]][cur[1]] == "L":
            prev = cur
            cur = cur[0], cur[1] + 1
        elif g[cur[0]][cur[1]] == "J":
            prev = cur
            cur = cur[0], cur[1] - 1
        else:
            prev = cur
            cur = cur[0] + 1, cur[1]

    elif prev == (cur[0], cur[1] - 1):  # right
        if g[cur[0]][cur[1]] == "7":
            prev = cur
            cur = cur[0] + 1, cur[1]
        elif g[cur[0]][cur[1]] == "J":
            prev = cur
            cur = cur[0] - 1, cur[1]
        else:
            prev = cur
            cur = cur[0], cur[1] + 1

    elif prev == (cur[0], cur[1] + 1):  # left
        if g[cur[0]][cur[1]] == "F":
            prev = cur
            cur = cur[0] + 1, cur[1]
        elif g[cur[0]][cur[1]] == "L":
            prev = cur
            cur = cur[0] - 1, cur[1]
        else:
            prev = cur
            cur = cur[0], cur[1] - 1

    return cur, prev


while cur != cur2:
    loop.append(cur)
    loop.append(cur2)
    print(cur, " ", prev)
    cur, prev = next_pipe(cur, prev)
    cur2, prev2 = next_pipe(cur2, prev2)
    out += 1

loop.append(cur)

# count the tiles outside the loop
outs = [(0, 0)]


print(out)
out2 = len(g) * len(g[0]) - (2 * out) - out2
print(out2)
