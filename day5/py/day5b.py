#!/usr/bin/env python3

with open("../input/input.txt") as file:
    jumps = [ int(x) for x in file.read().split() ]

x = 0
steps = 0
while x >= 0 and x < len(jumps):
    n = jumps[x]
    if n > 2:
        jumps[x] -= 1
    else:
        jumps[x] += 1
    steps += 1
    x+=n

print(steps)
