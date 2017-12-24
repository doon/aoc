#!/usr/bin/env python3

from itertools import combinations, permutations

valid = 0

with open("../input/input.txt") as file:
    for line in file:
        isValid = True
        words = line.strip().split()
        for a,b in combinations(words,2):
            if a in [''.join(p) for p in permutations(b)]:
                isValid = False

        if isValid:
            valid += 1
print(valid)

