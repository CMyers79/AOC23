
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
loop = set(start)
inside = set()

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


def next_pipe(cur, prev, first):
    if prev == (cur[0] + 1, cur[1]):  # up
        if g[cur[0]][cur[1]] == "F":
            if not first:
                for tile in [(cur[0], cur[1] - 1), (cur[0] - 1, cur[1] - 1), (cur[0] - 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0], cur[1] + 1
        elif g[cur[0]][cur[1]] == "7":
            if first:
                for tile in [(cur[0], cur[1] + 1), (cur[0] - 1, cur[1] + 1), (cur[0] - 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0], cur[1] - 1
        else:
            if first and (cur[0], cur[1] + 1) not in loop:
                inside.add((cur[0], cur[1] + 1))
            elif not first and (cur[0], cur[1] - 1) not in loop:
                inside.add((cur[0], cur[1] - 1))
            prev = cur
            cur = cur[0] - 1, cur[1]

    elif prev == (cur[0] - 1, cur[1]):  # down
        if g[cur[0]][cur[1]] == "L":
            if first:
                for tile in [(cur[0], cur[1] - 1), (cur[0] + 1, cur[1] - 1), (cur[0] + 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0], cur[1] + 1
        elif g[cur[0]][cur[1]] == "J":
            if not first:
                for tile in [(cur[0], cur[1] + 1), (cur[0] + 1, cur[1] + 1), (cur[0] + 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0], cur[1] - 1
        else:
            if first and (cur[0], cur[1] - 1) not in loop:
                inside.add((cur[0], cur[1] - 1))
            elif not first and (cur[0], cur[1] + 1) not in loop:
                inside.add((cur[0], cur[1] + 1))
            prev = cur
            cur = cur[0] + 1, cur[1]

    elif prev == (cur[0], cur[1] - 1):  # right
        if g[cur[0]][cur[1]] == "7":
            if not first:
                for tile in [(cur[0], cur[1] + 1), (cur[0] - 1, cur[1] + 1), (cur[0] - 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0] + 1, cur[1]
        elif g[cur[0]][cur[1]] == "J":
            if first:
                for tile in [(cur[0], cur[1] + 1), (cur[0] + 1, cur[1] + 1), (cur[0] + 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0] - 1, cur[1]
        else:
            if first and (cur[0] + 1, cur[1]) not in loop:
                inside.add((cur[0] + 1, cur[1]))
            elif not first and (cur[0] - 1, cur[1]) not in loop:
                inside.add((cur[0] - 1, cur[1]))
            prev = cur
            cur = cur[0], cur[1] + 1

    elif prev == (cur[0], cur[1] + 1):  # left
        if g[cur[0]][cur[1]] == "F":
            if first:
                for tile in [(cur[0], cur[1] - 1), (cur[0] - 1, cur[1] - 1), (cur[0] - 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0] + 1, cur[1]
        elif g[cur[0]][cur[1]] == "L":
            if not first:
                for tile in [(cur[0], cur[1] - 1), (cur[0] + 1, cur[1] - 1), (cur[0] + 1, cur[1])]:
                    if tile not in loop:
                        inside.add(tile)
            prev = cur
            cur = cur[0] - 1, cur[1]
        else:
            if first and (cur[0] - 1, cur[1]) not in loop:
                inside.add((cur[0] - 1, cur[1]))
            elif not first and (cur[0] + 1, cur[1]) not in loop:
                inside.add((cur[0] + 1, cur[1]))
            prev = cur
            cur = cur[0], cur[1] - 1

    if cur in inside:
        inside.remove(cur)
    return cur, prev


while cur != cur2:
    loop.add(cur)
    loop.add(cur2)
    cur, prev = next_pipe(cur, prev, True)
    cur2, prev2 = next_pipe(cur2, prev2, False)
    out += 1

loop.add(cur)

# inside may contain the tiles outside the loop if the first direction is counterclockwise

fill = set()

def in_search(c):
    for pair in adj.values():
        n = (c[0] + pair[0], c[1] + pair[1])
        if n not in loop and n not in inside | fill and 0 <= n[0] < len(g) and 0 <= n[1] < len(g[0]):
            fill.add(n)
            in_search(n)


for tile in inside:
    in_search(tile)

print(out)
print(len(inside | fill) - len(fill & loop) - len(inside & loop))
