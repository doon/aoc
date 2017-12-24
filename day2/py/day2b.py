#!/usr/bin/env python3

from itertools import permutations

checksum = 0

with open("../input/input.txt") as file:
    for line in file:
        nums = [int(n) for n in line.strip().split()]
        for x,y in permutations(nums,2):
            if x % y == 0:
                checksum += int(x/y)

print(checksum)
