
with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
bricks = []
stack = []
for i, s in enumerate(s_list):
    end1 = s.split("~")[0].split(",")
    end2 = s.split("~")[1].split(",")
    bricks.append([int(end1[0]), int(end1[1]), int(end1[2]), int(end2[0]), int(end2[1]), int(end2[2])])


def fall(i, stack):
    brick_coords = []
    if bricks[i][0] != bricks[i][3]:
        for x in range(bricks[i][0], bricks[i][3] + 1):
            brick_coords.append([x, bricks[i][1], bricks[i][2]])
    elif bricks[i][1] != bricks[i][4]:
        for y in range(bricks[i][1], bricks[i][4] + 1):
            brick_coords.append([bricks[i][0], y, bricks[i][2]])
    elif bricks[i][2] != bricks[i][5]:
        for z in range(bricks[i][2], bricks[i][5] + 1):
            brick_coords.append([bricks[i][0], bricks[i][1], z])
    else:
        brick_coords.append([bricks[i][0], bricks[i][1], bricks[i][2]])

    fell = False
    min_z = min([coord[2] for coord in brick_coords])
    if min_z == 0:
        return brick_coords, fell

    for _ in range(min_z):
        for coord in brick_coords:
            for brick in stack:
                if [coord[0], coord[1], coord[2] - 1] in brick:
                    return brick_coords, fell

        for coord in brick_coords:
            coord[2] -= 1
            fell = True
        min_z = min([coord[2] for coord in brick_coords])
        if min_z == 0:
            return brick_coords, fell


bricks.sort(key=lambda x: min(x[2], x[5]))
for i in range(len(bricks)):
    result = fall(i, stack)
    stack.append(result[0])

bricks = [[brick[0][0], brick[0][1], brick[0][2], brick[-1][0], brick[-1][1], brick[-1][2]] for brick in stack]
bricks.sort(key=lambda x: min(x[2], x[5]))

out = 0
for brick in bricks:
    bricks2 = [brick2 for brick2 in bricks if brick2[0] != brick[0] or brick2[1] != brick[1] or brick2[2] != brick[2]]

    stack2 = [brick2 for brick2 in stack if [brick[0], brick[1], brick[2]] != brick2[0] and [brick[0], brick[1], brick[2]] != brick2[-1]]

    fell = False
    for i in range(len(bricks2)):
        if fall(i, stack2)[1]:
            fell = True
            break
    if fell:
        continue
    out += 1
    print(out)

print(out)
