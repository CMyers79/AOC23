with open('input2.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
s_list.append("")
out = 0
i = 0
j = 0
while i < len(s_list) - 1:
    i += 1
    if len(s_list[i]) == 0:
        f = s_list[j:i]
        found = False
        # find horizontal reflection line
        for k, line in enumerate(f):
            for m in range(k + 1, len(f)):
                if f[m] == line and (k == 0 or m == len(f) - 1):
                    found = True
                    for n in range(k + 1, m):
                        if f[n] != f[m - n + k]:
                            found = False
                            break
                    if found:
                        out += 100 * (k + (m - k + 1) // 2)
                        print(k, m, out)
                        break
            if found:
                break
        g = []
        for k in range(len(f[0])):
            g.append("".join([f[l][k] for l in range(len(f))]))
        found = False
        for k, line in enumerate(g):
            for m in range(k + 1, len(g)):
                if g[m] == line and (k == 0 or m == len(g) - 1):
                    found = True
                    for n in range(k + 1, m):
                        if g[n] != g[m - n + k]:
                            found = False
                            break
                    if found:
                        out += k + (m - k + 1) // 2
                        print(k, m, out)
                        break
            if found:
                break

        j = i + 1
        print(out)
        print(f)
        print(g)

print(out)
