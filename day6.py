from collections import defaultdict
from collections import deque

with open('input2.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]

# times = [int(time) for time in s_list[0].split(" ")[1:] if time != '']
# dists = [int(time) for time in s_list[1].split(" ")[1:] if time != '']

times = [50748685]
dists = [242101716911252]

out = 1

for i, t in enumerate(times):
    n = 0
    for j in range(t):
        s = j * (t - j)
        if s > dists[i]:
            n += 1

    out *= n

print(out)

