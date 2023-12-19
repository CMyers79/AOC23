import sys

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]

heatmap = []
for i, s in enumerate(s_list):
    heatmap.append([])
    for char in s:
        heatmap[i].append(int(char))

visited = [[False for _ in range(len(heatmap[0]))] for _ in range(len(heatmap))]
dist = [[sys.maxsize for _ in range(len(heatmap[0]))] for _ in range(len(heatmap))]
prev = [[['a', 'b', 'c'] for _ in range(len(heatmap[0]))] for _ in range(len(heatmap))]
dist[0][0] = 0
adj = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1), 'src': (0, 0)}

done = False
while not done:
    min_dist = sys.maxsize
    min_cell = None
    min_dir = None
    for i in range(len(visited)):
        for j in range(len(visited)):
            for cell in adj.keys():
                if 0 <= i + adj[cell][0] < len(visited) and 0 <= j + adj[cell][1] < len(visited[0]):
                    if cell != prev[i][j][0] or cell != prev[i][j][1] or cell != prev[i][j][2]:
                        if dist[i + adj[cell][0]][j + adj[cell][1]] < min_dist and not visited[i + adj[cell][0]][j + adj[cell][1]]:
                            # print(i, " ", j)
                            min_dist = dist[i + adj[cell][0]][j + adj[cell][1]]
                            min_dir = cell
                            min_cell = [i + adj[cell][0], j + adj[cell][1]]

    if min_cell is not None:
        visited[min_cell[0]][min_cell[1]] = True
        prev[min_cell[0]][min_cell[1]] = prev[min_cell[0]][min_cell[1]][1:] + [min_dir]
    else:
        print("Error")
        break

    for cell in adj.keys():
        row = min_cell[0] + adj[cell][0]
        col = min_cell[1] + adj[cell][1]
        if 0 <= row < len(visited) and 0 <= col < len(visited[0]):
            if not visited[row][col]:
                if cell != prev[min_cell[0]][min_cell[1]][0] or cell != prev[min_cell[0]][min_cell[1]][1] or cell != prev[min_cell[0]][min_cell[1]][2]:
                    if dist[row][col] > min_dist + heatmap[row][col]:
                        dist[row][col] = min_dist + heatmap[row][col]

    done = True
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if not visited[i][j]:
                done = False
                break

print(dist[-1][-1])
