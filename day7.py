from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()
s_list = [string.strip() for string in strings]
out = 0
out2 = 0
hands = []
for i, s in enumerate(s_list):
    line = s.split(" ")
    hands.append([line[0], int(line[1])])

# rank hand types
for hand in hands:
    cards = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0,
             "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
    for card in hand[0]:
        cards[card] += 1

    # c_v = [v for v in cards.values()]
    # c_v.sort(reverse=True)

    non_wild_cards = {key: val for key, val in cards.items() if key != "J"}
    wilds = cards["J"]

    c_v = [v for v in non_wild_cards.values()]
    c_v.sort(reverse=True)
    c_v[0] += wilds

    if c_v[0] == 5:
        hand.append(5)
    elif c_v[0] == 4:
        hand.append(4)
    elif c_v[0] == 3 and c_v[1] == 2:
        hand.append(3.5)
    elif c_v[0] == 3:
        hand.append(3)
    elif c_v[:3] == [2, 2, 1]:
        hand.append(2.5)
    elif c_v[0] == 2:
        hand.append(2)
    else:
        hand.append(1)

for hand in hands:
    hand[0] = [char for char in hand[0]]
    for i, char in enumerate(hand[0]):
        if char == 'A':
            hand[0][i] = 14
        elif char == 'K':
            hand[0][i] = 13
        elif char == 'Q':
            hand[0][i] = 12
        elif char == 'J':
            hand[0][i] = 1
        elif char == 'T':
            hand[0][i] = 10
        else:
            hand[0][i] = int(char)

print(hands)
sorted_hands = []
fives = [hand for hand in hands if hand[2] == 5]
fours = [hand for hand in hands if hand[2] == 4]
fulls = [hand for hand in hands if hand[2] == 3.5]
threes = [hand for hand in hands if hand[2] == 3]
twops = [hand for hand in hands if hand[2] == 2.5]
pairs = [hand for hand in hands if hand[2] == 2]
highs = [hand for hand in hands if hand[2] == 1]

for i in range(5):
    fives.sort(key=lambda x: x[0][4 - i])
    fours.sort(key=lambda x: x[0][4 - i])
    fulls.sort(key=lambda x: x[0][4 - i])
    threes.sort(key=lambda x: x[0][4 - i])
    twops.sort(key=lambda x: x[0][4 - i])
    pairs.sort(key=lambda x: x[0][4 - i])
    highs.sort(key=lambda x: x[0][4 - i])

for high in highs:
    sorted_hands.append(high)
for pair in pairs:
    sorted_hands.append(pair)
for twop in twops:
    sorted_hands.append(twop)
for three in threes:
    sorted_hands.append(three)
for full in fulls:
    sorted_hands.append(full)
for four in fours:
    sorted_hands.append(four)
for five in fives:
    sorted_hands.append(five)

print(sorted_hands)

for i, hand in enumerate(sorted_hands):
    out += (i + 1) * hand[1]

print(out)
