with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
universe = []
empty_rows = []
for i, s in enumerate(s_list):
    universe.append([])
    for c in s:
        universe[-1].append(c)
    if '#' not in s:
        # universe.append([])
        # for c in s:
        #     universe[-1].append(c)
        empty_rows.append(i)

empty_cols = []
for j in range(len(universe[0])):
    empty = True
    for k in range(len(universe)):
        if universe[k][j] == '#':
            empty = False
    if empty:
        empty_cols.append(j)

# for i in range(len(empty_cols)):
#     for j in range(len(universe)):
#         universe[j].insert(empty_cols[len(empty_cols) - i - 1], '.')

galaxies = []
for i in range(len(universe)):
    for j in range(len(universe[0])):
        if universe[i][j] == '#':
            galaxies.append((i, j))

pairs = set()
for g in galaxies:
    for t in galaxies:
        if t != g and (t, g) not in pairs:
            pairs.add((g, t))

for pair in pairs:
    h = 0
    v = 0
    for r in empty_rows:
        if min(pair[0][0], pair[1][0]) < r < max(pair[0][0], pair[1][0]):
            v += 999999
    for c in empty_cols:
        if min(pair[0][1], pair[1][1]) < c < max(pair[0][1], pair[1][1]):
            h += 999999
    out += abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) + h + v

print(out)
