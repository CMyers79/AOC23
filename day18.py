
with open('input2.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
direction = []
dist = []
color = []
for i, s in enumerate(s_list):
    line = s.split(" ")
    # direction.append(line[0])
    # dist.append(line[1])
    color.append(line[2][2:-1])

for line in color:
    if line[-1] == '0':
        direction.append('R')
    elif line[-1] == '1':
        direction.append('D')
    elif line[-1] == '2':
        direction.append('L')
    elif line[-1] == '3':
        direction.append('U')

    dist.append(int(line[:-1], 16))


#
# grid = [['.' for _ in range(800)] for _ in range(800)]
#
# cur = [12, 12]
# grid[cur[0]][cur[1]] = 'O'
# for i in range(len(direction)):
#     if direction[i] == "U":
#         for j in range(int(dist[i])):
#             cur[0] -= 1
#             grid[cur[0]][cur[1]] = 'O'
#     elif direction[i] == "D":
#         for j in range(int(dist[i])):
#             cur[0] += 1
#             grid[cur[0]][cur[1]] = 'O'
#     elif direction[i] == "R":
#         for j in range(int(dist[i])):
#             cur[1] += 1
#             grid[cur[0]][cur[1]] = 'O'
#     elif direction[i] == "L":
#         for j in range(int(dist[i])):
#             cur[1] -= 1
#             grid[cur[0]][cur[1]] = 'O'
#
#
# def flip_cell(cur, limit=990):
#     cells = []
#     if limit > 0:
#         for cell in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#             if 0 <= cur[0] + cell[0] < len(grid) and 0 <= cur[1] + cell[1] < len(grid[0]):
#                 if grid[cur[0] + cell[0]][cur[1] + cell[1]] == '.':
#                     grid[cur[0] + cell[0]][cur[1] + cell[1]] = 'X'
#                     next_cell = flip_cell((cur[0] + cell[0], cur[1] + cell[1]), limit - 1)
#                     if next_cell is not None:
#                         cells += next_cell
#
#         if len(cells) > 0:
#             return cells
#
#     else:
#         return [cur]
#
#
# next_cells = flip_cell((0, 0), 990)
# while len(next_cells) > 0:
#     end_cells = []
#     for cell in next_cells:
#         result = flip_cell(cell, 990)
#         if result is not None:
#             end_cells += result
#     next_cells = end_cells
#
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] in ['.', 'O']:
#             out += 1
#
# print(out)
