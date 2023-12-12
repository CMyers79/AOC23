from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
for i, s in enumerate(s_list):
    springs = s.split(" ")[0]
    groups = [int(num) for num in s.split(" ")[1].split(",")]
    given = []
    qs = []
    j = 0
    while j < len(springs):
        if springs[j] == '#':
            given.append(1)
            j += 1
        elif springs[j] == ".":
            given.append(0)
            j += 1
        elif springs[j] == "?":
            given.append(-1)
            qs.append(j)
            j += 1

    for c in range(2 ** len(qs)):
        seq = f"{c:0{len(qs)}b}"

        for k, q in enumerate(qs):
            given[q] = int(seq[k])

        cur_groups = []
        n = 0
        f = 0
        for g, d in enumerate(given):
            if d == 1:
                n += 1
                f = 1
                if g == len(given) - 1:
                    cur_groups.append(n)
            else:
                if f == 1:
                    cur_groups.append(n)
                    n = 0
                    f = 0

        if cur_groups == groups:
            out += 1

print(out)
print(out2)
