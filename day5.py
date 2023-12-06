from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]

seeds = [[int(seed) for seed in s_list[0][7:].split(" ")]]

maps = s_list[2:]

i = 0
j = 0

while i < len(maps):
    s = []
    d = []
    seeds.append([])
    while maps[i] == '' or not maps[i][0].isdigit():
        i += 1
    while i < len(maps) and maps[i] != '':
        destination, source, _range = maps[i].split(" ")[0], maps[i].split(" ")[1], maps[i].split(" ")[2]
        d.append((int(destination), int(destination) + int(_range)))
        s.append((int(source), int(source) + int(_range)))
        i += 1

    for n, seed in enumerate(seeds[j]):

        for k in range(len(d)):
            if s[k][0] <= seed <= s[k][1]:
                seeds[j + 1].append(d[k][0] + seed - s[k][0])
                break
        if len(seeds[j + 1]) <= n:
            seeds[j + 1].append(seed)

    j += 1

print(min(seeds[-1]))
