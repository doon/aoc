#!/usr/bin/env python3

checksum = 0

with open(".//input/input.txt") as file:
    for line in file:
        nums = [int(n) for n in line.strip().split()]
        mx = max(nums)
        mn = min(nums)
        checksum += (mx - mn)

print(checksum)
