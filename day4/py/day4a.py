#!/usr/bin/env python3

valid = 0

with open("../input/input.txt") as file:
    for line in file:
        words = line.strip().split()
        if len(set(words)) == len(words):
            valid += 1
print(valid)

