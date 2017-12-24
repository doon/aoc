#!/usr/bin/env python3

with open("../input/input.txt") as file:
    jumps = [ int(x) for x in file.read().split() ]

x = 0
steps = 0
while x >= 0 and x < len(jumps):
    n = jumps[x]
    jumps[x] += 1
    steps += 1
    x+=n

print(steps)
