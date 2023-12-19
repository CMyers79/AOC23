from collections import defaultdict
from collections import deque

with open('input2.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
i = 0
while i < len(s_list):
    cur = []
    found = False
    while s_list[i] != "":
        cur.append(s_list[i])
        i += 1
    for j in range(1, len(cur), 2):
        if cur[0] == cur[j]:
            match = True
            for k in range(1, (j + 1) // 2):
                if cur[k] != cur[j - k]:
                    match = False
            if match:
                out += 100 * (j + 1) // 2
                found = True
                break
    if not found:
        for j in range(len(cur) - 2, -1, -2):
            if cur[j] == cur[-1]:
                match = True
                for k in range(len(cur) - 2, j + (len(cur) - j) // 2, -1):
                    if cur[k] != cur[k - j]:
                        match = False

    i += 1



print(out)
print(out2)