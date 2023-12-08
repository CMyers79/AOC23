from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0

d = s_list[0]
a = {}
c = {}
s_list = s_list[2:]
t = []
for i, s in enumerate(s_list):
    a[s_list[i][:3]] = (s_list[i][7:10], s_list[i][12:15])

ghosts = [key for key in a.keys() if key[2] == 'A']
for ghost in ghosts:
    cur = ghost
    while cur[2] != 'Z':
        for b in d:
            if b == 'L':
                cur = a[cur][0]
            else:
                cur = a[cur][1]

        out += 1

    t.append(out)
    out = 0

out2 = 1
for o in t:
    out2 *= o
out2 *= len(d)
print(out2)
