from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
for i, s in enumerate(s_list):
    nums = [[int(num) for num in s.split(" ")]]
    done = False
    while not done:
        nums.append([nums[-1][j] - nums[-1][j - 1] for j in range(1, len(nums[-1]))])
        if nums[-1] == [0 for _ in range(len(nums[-1]))]:
            done = True

    nums[-1].append(0)
    for j in range(2, len(nums) + 1):
        nums[-j].append(nums[-j + 1][-1] + nums[-j][-1])
        nums[-j].insert(0, nums[-j][0] - nums[-j + 1][0])

    out += nums[0][-1]
    out2 += nums[0][0]
print(out)
print(out2)
