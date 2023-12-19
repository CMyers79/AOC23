with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out2 = 0


def combos(gr, qs_, giv):
    out = 0
    for c in range(2 ** len(qs_)):
        seq = f"{c:0{len(qs_)}b}"

        for k, q in enumerate(qs_):
            giv[q] = int(seq[k])

        cur_groups = []
        n = 0
        f = 0
        for g, d in enumerate(giv):
            if d == 1:
                n += 1
                f = 1
                if g == len(giv) - 1:
                    cur_groups.append(n)
            elif f == 1:
                cur_groups.append(n)
                n = 0
                f = 0

        if cur_groups == gr:
            out += 1
    return out


for i, s in enumerate(s_list):
    springs = s.split(" ")[0]
    groups = [int(num) for num in s.split(" ")[1].split(",")]
    groups2 = groups + groups
    given = []
    qs = []
    j = 0
    while j < len(springs):
        if springs[j] == '#':
            given.append(1)
            j += 1
        elif springs[j] == '.':
            given.append(0)
            j += 1
        elif springs[j] == '?':
            given.append(2)
            qs.append(j)
            j += 1

    given2 = given + [2] + given
    qs2 = qs + [qs[-1] + 1] + [q + qs[-1] + 2 for q in qs]

    combos1 = combos(groups, qs, given)
    combos4 = combos(groups2, qs2, given2)

    out2 += combos1 * (combos4 - combos1) ** 4
    print(out2)

print('{:f}'.format(out2))
