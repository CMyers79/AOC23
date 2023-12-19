with open('input3.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
steps = s_list[0].split(",")
for step in steps:
    cur = 0
    for char in step:
        cur = (cur + ord(char)) * 17 % 256
    out += cur

boxes = [[] for _ in range(256)]

for step in steps:
    i = 0
    while step[i] not in "=-":
        i += 1
    box = 0
    for char in step[:i]:
        box = (box + ord(char)) * 17 % 256
    if step[i] == '-' and step[:i] in [pair[0] for pair in boxes[box]]:
        boxes[box] = [pair for pair in boxes[box] if pair[0] != step[:i]]
    elif step[i] == '=' and step[:i] not in [pair[0] for pair in boxes[box]]:
        boxes[box].append([step[:i], int(step[-1])])
    elif step[i] == '=':
        for pair in boxes[box]:
            if pair[0] == step[:i]:
                pair[1] = int(step[-1])
    else:
        continue

for j in range(256):
    for k in range(len(boxes[j])):
        out2 += (j + 1) * (k + 1) * boxes[j][k][1]

print(out)
print(out2)
