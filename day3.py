from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
a = []
d = []
pn = []
gears = []
out = 0
out2 = 0
for i, s in enumerate(s_list):
    d.append([])
    for c in s:
        d[i].append(c)

for i, s in enumerate(s_list):
    pn.append("")
    g = False
    for j, c in enumerate(s):
        if c.isdigit():
            f = False
            hb = max(0, j - 1)
            he = min(len(s) - 1, j + 2)
            vb = max(0, i - 1)
            ve = min(len(s_list), i + 2)
            for row in range(vb, ve):
                for col in range(hb, he):
                    if d[row][col] not in ".0123456789":
                        f = True
                        g = True
            if f or g:
                pn[i] = pn[i] + c
                k = 0
                while j - k >= 0 and d[i][j-k].isdigit():
                    pn[i] = pn[i][:j-k] + d[i][j-k] + pn[i][j-k+1:]
                    k += 1
            else:
                pn[i] = pn[i] + "."

        elif c == ".":
            g = False
            pn[i] = pn[i] + "."

        elif c == "*":
            h = 0
            k = []
            hb = max(0, j - 1)
            he = min(len(s) - 1, j + 1)
            vb = max(0, i - 1)
            ve = min(len(s_list), i + 1)

            for row in range(vb, ve + 1):
                if he - hb == 2 and d[row][hb].isdigit() and d[row][he].isdigit() and not d[row][hb + 1].isdigit():
                    h += 2
                    k.append((row, 2))
                elif not d[row][hb].isdigit() and not d[row][he].isdigit() and not d[row][hb + 1].isdigit():
                    continue
                else:
                    h += 1
                    k.append((row, 1))

            if h == 2:
                gears.append((i, j, k))

            pn[i] = pn[i] + "."

        else:
            pn[i] = pn[i] + "."

for i in pn:
    pns = i.split(".")
    for x in pns:
        if x != '':
            out += int(x)

for gear in gears:
    print(gear)
    first = 0
    for row in gear[2]:
        if row[1] == 2:
            m = 0
            n = 0
            sa = ""
            sb = ""
            while d[row[0]][gear[1] - m - 1].isdigit():
                sa = d[row[0]][gear[1] - m - 1] + sa
                m += 1

            while d[row[0]][gear[1] + n + 1].isdigit():
                sb = sb + d[row[0]][gear[1] + n + 1]
                n += 1

            out2 += int(sa) * int(sb)
            print(int(sa), " ", int(sb))
            break

        elif row[1] == 1:
            n = -1
            sa = ""

            while gear[1] + n < len(d[row[0]]) and not d[row[0]][gear[1] + n].isdigit():
                print(d[row[0]][gear[1] + n])
                n += 1
            while gear[1] + n >= 0 and d[row[0]][gear[1] + n - 1].isdigit():
                print(d[row[0]][gear[1] + n])
                n -= 1
            while gear[1] + n < len(d[row[0]]) and d[row[0]][gear[1] + n].isdigit():
                print(d[row[0]][gear[1] + n])
                sa = sa + d[row[0]][gear[1] + n]
                n += 1

            if first == 0:
                first = int(sa)
            else:
                out2 += first * int(sa)
                print(first, " ", int(sa))
                break

print(out)
print(out2)
