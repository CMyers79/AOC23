with open('input2.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
direction = []
dist = []
color = []
for i, s in enumerate(s_list):
    line = s.split(" ")
    color.append(line[2][2:-1])

for line in color:
    if line[-1] == '0':  # to the right, the loop is clockwise
        direction.append(0)
    elif line[-1] == '1':
        direction.append(1)
    elif line[-1] == '2':
        direction.append(2)
    elif line[-1] == '3':
        direction.append(3)

    dist.append(int(line[:-1], 16))

h_coord = 0
v_coord = 0
edges = []
prev = None
for d in range(len(direction)):
    if direction[d] == 0:
        prev = h_coord
        h_coord += dist[d]
    elif direction[d] == 1:
        prev = v_coord
        v_coord += dist[d]
    elif direction[d] == 2:
        prev = h_coord
        h_coord -= dist[d]
    elif direction[d] == 3:
        prev = v_coord
        v_coord -= dist[d]

    edges.append([direction[d], prev, h_coord, v_coord])

top = min([edge[3] for edge in edges if edge[0] == 0])
right = max([edge[2] for edge in edges if edge[0] == 1])
bottom = max([edge[3] for edge in edges if edge[0] == 2])
left = min([edge[2] for edge in edges if edge[0] == 3])

out = (1 + right - left) * (1 + bottom - top)
tops = []
rights = []
bottoms = []
lefts = []

for i, edge in enumerate(edges):
    if edges[i][3] == top and edges[i][0] == 0:
        if len(tops) == 0:
            first_top = i
        tops.append(i - first_top)
    elif edges[i][2] == right and edges[i][0] == 1:
        rights.append(i - first_top)
    elif edges[i][3] == bottom and edges[i][0] == 2:
        bottoms.append(i - first_top)
    elif edges[i][2] == left and edges[i][0] == 3:
        lefts.append(i - first_top)

edges = edges[first_top:] + edges[:first_top]
cur_top = tops[0]

for j in range(1, len(tops) - 1):
    next_top = tops[j]

    for k in range(cur_top + 1, next_top):
        if direction[k] == 1:
            out -= dist[k] * (edges[next_top][1] - edges[k][2] + 1)
        elif direction[k] == 3:
            out += dist[k] * (edges[next_top][1] - edges[k][2])

    cur_top = next_top

next_top = rights[0]

for k in range(cur_top + 1, next_top):
    if direction[k] == 1:
        out -= dist[k] * (edges[next_top][2] - edges[k][2])
    elif direction[k] == 3:
        out += dist[k] * (edges[next_top][2] - edges[k][2] + 1)

cur_top = rights[0]
for j in range(1, len(rights) - 1):
    next_top = rights[j]

    for k in range(cur_top + 1, next_top):
        if direction[k] == 2:
            out -= dist[k] * (edges[next_top][1] - edges[k][3] + 1)
        elif direction[k] == 0:
            out += dist[k] * (edges[next_top][1] - edges[k][3])

    cur_top = next_top

next_top = bottoms[0]

for k in range(cur_top + 1, next_top):
    if direction[k] == 2:
        out -= dist[k] * (edges[next_top][3] - edges[k][3])
    elif direction[k] == 0:
        out += dist[k] * (edges[next_top][3] - edges[k][3] + 1)

cur_top = bottoms[0]
for j in range(1, len(bottoms) - 1):
    next_top = bottoms[j]

    for k in range(cur_top + 1, next_top):
        if direction[k] == 3:
            out -= dist[k] * (edges[k][2] - edges[next_top][1] + 1)
        elif direction[k] == 1:
            out += dist[k] * (edges[k][2] - edges[next_top][1])

    cur_top = next_top

next_top = lefts[0]

for k in range(cur_top + 1, next_top):
    if direction[k] == 3:
        out -= dist[k] * (edges[k][2] - edges[next_top][2])
    elif direction[k] == 1:
        out += dist[k] * (edges[k][2] - edges[next_top][2] + 1)

cur_top = lefts[0]

for j in range(1, len(lefts) - 1):
    next_top = lefts[j]

    for k in range(cur_top + 1, next_top):
        if direction[k] == 0:
            out -= dist[k] * (edges[k][3] - edges[next_top][1] + 1)
        elif direction[k] == 2:
            out += dist[k] * (edges[k][3] - edges[next_top][1])

    cur_top = next_top

for k in range(cur_top + 1, len(edges)):
    if direction[k] == 0:
        out -= dist[k] * (edges[k][3] - edges[0][1])
    elif direction[k] == 2:
        out += dist[k] * (edges[k][3] - edges[0][1] + 1)

print(out)
