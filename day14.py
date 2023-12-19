with open('input3.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
p = []
for i, s in enumerate(s_list):
    p.append([])
    for char in s:
        p[i].append(char)

for n in range(1000000000):
    # north
    for j in range(len(p) - 1):
        for k in range(1, len(p) - j):
            for i in range(len(p[0])):
                if p[k][i] == 'O' and p[k - 1][i] == ".":
                    p[k - 1][i] = 'O'
                    p[k][i] = "."

    # west
    for j in range(len(p[0]) - 1):
        for k in range(1, len(p[0]) - j):
            for i in range(len(p)):
                if p[i][k] == 'O' and p[i][k - 1] == '.':
                    p[i][k] = '.'
                    p[i][k - 1] = 'O'

    # south
    for j in range(len(p) - 1):
        for k in range(len(p) - j - 2, 0, -1):
            for i in range(len(p[0])):
                if p[k][i] == 'O' and p[k + 1][i] == ".":
                    p[k + 1][i] = 'O'
                    p[k][i] = "."

    # east
    for j in range(len(p[0]) - 1):
        for k in range(len(p[0]) - j - 2, 0, -1):
            for i in range(len(p)):
                if p[i][k] == 'O' and p[i][k + 1] == '.':
                    p[i][k] = '.'
                    p[i][k + 1] = 'O'

    if done:
        print(n)
        break

for i in range(len(p)):
    for j in p[i]:
        if j == 'O':
            out += len(p) - i

print(out)
