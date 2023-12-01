from collections import defaultdict
from collections import deque

with open('input.txt') as file:
    strings = file.readlines()

num = None
out = 0

numwords = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

for i in range(len(strings)):
    for j in range(len(strings[i])):
        c = strings[i][j]
        if c in "0123456789":
            num = int(c) * 10
            break
        elif 1 < j < len(strings[i]) - 1 and strings[i][j - 2:j + 1] in numwords.keys():
            c = numwords[strings[i][j - 2:j + 1]]
            num = c * 10
            break
        elif 2 < j < len(strings[i]) - 1 and strings[i][j - 3:j + 1] in numwords.keys():
            c = numwords[strings[i][j - 3:j + 1]]
            num = c * 10
            break
        elif 3 < j < len(strings[i]) - 1 and strings[i][j - 4:j + 1] in numwords.keys():
            c = numwords[strings[i][j - 4:j + 1]]
            num = c * 10
            break

    for k in range(len(strings[i])):
        d = strings[i][len(strings[i]) - k - 1]
        if d in "0123456789":
            num += int(d)
            break
        elif 1 < k < len(strings[i]) - 1 and strings[i][len(strings[i]) - k - 1:len(strings[i]) - k + 2] in numwords.keys():
            d = numwords[strings[i][len(strings[i]) - k - 1:len(strings[i]) - k + 2]]
            num += d
            break
        elif 2 < k < len(strings[i]) - 1 and strings[i][len(strings[i]) - k - 1:len(strings[i]) - k + 3] in numwords.keys():
            d = numwords[strings[i][len(strings[i]) - k - 1:len(strings[i]) - k + 3]]
            num += d
            break
        elif 3 < k < len(strings[i]) - 1 and strings[i][len(strings[i]) - k - 1:len(strings[i]) - k + 4] in numwords.keys():
            d = numwords[strings[i][len(strings[i]) - k - 1:len(strings[i]) - k + 4]]
            num += d
            break

    print(c, " ", d, " ", num)
    out += num

print(out)


