import math

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
seeds_and_ranges = [int(seed) for seed in s_list[0][7:].split(" ")]

# convert seed ranges to from "start length" to (start, end)
seeds = seeds_and_ranges[::2]
ranges = seeds_and_ranges[1::2]
seed_ranges = [(seeds[i], seeds[i] + ranges[i]) for i in range(len(seeds))]

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

# populate array with maps sorted ascending by destination range, removing empty lists between maps
while i < len(map_array):
    j = i
    while j < len(map_array) and len(map_array[j]) > 0:
        j += 1

    sorted_maps.append(sorted(map_array[i:j], key=lambda x: x[0][0]))
    i = j
    while len(map_array[i]) == 0:
        i += 1

# explicitly define and insert unmapped source ranges in each map
for n in range(len(sorted_maps)):
    p = 0
    while p < len(sorted_maps[n]) - 1:
        if sorted_maps[n][p + 1][1][0] > sorted_maps[n][p][1][1]:
            sorted_maps[n].insert(p + 1, [(sorted_maps[n][p][1][1], sorted_maps[n][p + 1][1][0]),
                                          (sorted_maps[n][p][1][1], sorted_maps[n][p + 1][1][0])])


# recurse backwards through maps to find lowest location match
def traverse_maps(k, range_set):
    if k == 6:
        for s_range in seed_ranges:
            if s_range[0] <= range_set[0] < s_range[1]:
                return range_set[0]
            elif range_set[0] < s_range[0] < range_set[1]:
                return s_range[0]
            elif len(range_set) > 1:
                return traverse_maps(k, range_set[1:])
            else:
                return math.inf
    else:
        new_range = None
        new_range_2 = None
        for m_range in sorted_maps[k + 1]:
            if m_range[1][0] <= range_set[0] < m_range[1][1]:
                new_range = (m_range[0][0] + range_set[0] - m_range[1][0], min(m_range[0][1], m_range[0][0] + range_set[0] - m_range[1][0]))
                if range_set[1] > m_range[1][1]:
                    new_range_2 = (m_range[1][1], range_set[1])

        if new_range is not None:
            if new_range_2 is not None:
                return min(traverse_maps(k + 1, new_range), traverse_maps(k + 1, new_range_2))
            else:
                return traverse_maps(k + 1, new_range)

        else:
            print("error, range not found at depth ", k)

print(min())
