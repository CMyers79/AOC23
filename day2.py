from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()

out = 0
out2 = 0
f = True
for i, s in enumerate(strings):
    red = 0
    green = 0
    blue = 0
    c = s.split(": ")[1].strip()
    cs = c.split("; ")
    for co in cs:
        cos = co.split(", ")
        for col in cos:
            r = col.split(" ")
            q = int(r[0])
            if r[1] == "red" and q > 12 or r[1] == "green" and q > 13 or r[1] == "blue" and q > 14:
                f = False
            if r[1] == "red":
                red = max(red, q)
            elif r[1] == "green":
                green = max(green, q)
            else:
                blue = max(blue, q)

    if f:
        out += i + 1
    out2 += red * green * blue

    f = True

print(out, " ", out2)
