with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
seeds_and_ranges = [int(seed) for seed in s_list[0][7:].split(" ")]

# convert seed ranges to from "start length" to (start, end)
seeds = seeds_and_ranges[::2]
ranges = seeds_and_ranges[1::2]
seed_ranges = [(seeds[i], seeds[i] + ranges[i]) for i in range(len(seeds))]
print(seed_ranges)
# convert map range sets to lists, replace blank and descriptor lines with empty lists
maps = s_list[3:]
map_nums = []
for map_line in maps:
    if map_line != '' and map_line[0].isdigit():
        map_nums.append([int(num) for num in map_line.split(" ")])
    else:
        map_nums.append([])

# convert range list elements to tuples (destination start, destination end), (source start, source end)
# and reverse order of maps
map_array = []
for i in range(len(map_nums)):
    if len(map_nums[-i]) > 0:
        map_array.append([(map_nums[-i][0], map_nums[-i][0] + map_nums[-i][2]),
                          (map_nums[-i][1], map_nums[-i][1] + map_nums[-i][2])])
    else:
        map_array.append([])

i = 0
j = 0
sorted_maps = []

# populate array with maps sorted ascending by source range, removing empty lists between maps
while i < len(map_array):
    j = i
    while j < len(map_array) and len(map_array[j]) > 0:
        j += 1

    sorted_maps.append(sorted(map_array[i:j], key=lambda x: x[1][0]))
    i = j
    while i < len(map_array) and len(map_array[i]) == 0:
        i += 1

# explicitly define and insert unmapped source ranges in each map
for n in range(len(sorted_maps)):
    p = 0
    while p < len(sorted_maps[n]) - 1:
        if sorted_maps[n][p + 1][1][0] > sorted_maps[n][p][1][1]:
            sorted_maps[n].insert(p + 1, [(sorted_maps[n][p][1][1], sorted_maps[n][p + 1][1][0]),
                                          (sorted_maps[n][p][1][1], sorted_maps[n][p + 1][1][0])])
            p += 1
        p += 1

# sort array by destination range
for _map in sorted_maps:
    _map.sort(key=lambda x: x[0][0])

done = False
for range_pair in sorted_maps[0]:
    for source in range(range_pair[1][0], range_pair[1][1]):
        if not done:
            n = source
            for i in range(1, 7):
                j = 0
                while j < len(sorted_maps[i]) and not sorted_maps[i][j][0][0] <= n < sorted_maps[i][j][0][1]:
                    j += 1
                if j < len(sorted_maps[i]):
                    offset = n - sorted_maps[i][j][0][0]
                    n = sorted_maps[i][j][1][0] + offset
                else:
                    continue

            print(n)
            for s_range in seed_ranges:
                if s_range[0] <= n < s_range[1]:
                    print(n)
                    done = True
                    break
        else:
            break
