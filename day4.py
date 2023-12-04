from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
cards = [1 for i in range(len(s_list))]
for i, s in enumerate(s_list):
    nums = s.split("|")
    wins = nums[0].split(" ")
    plays = nums[1].split(" ")
    score = [play for play in plays if play in wins and play != '']
    out += 2**(len(score) - 1) // 1

    for j in range(len(score)):
        for _ in range(cards[i]):
            if i + j < len(s_list):
                cards[i + j + 1] += 1

for card in cards:
    out2 += card

print(out)
print(out2)
