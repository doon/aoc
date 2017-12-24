#!/usr/bin/env python3

states = []
done = False

with open("../input/input.txt") as file:
   banks = [ int(x) for x in file.read().split() ]

state = ' '.join(str(b) for b in banks)

while state not in states:
    states.append(state)
    start = banks.index(max(banks))
    blocks = banks[start]
    banks[start] = 0
    start += 1
    end = start+blocks
    for i in range(start,end):
        banks[i % 16] += 1
    state = ' '.join(str(b) for b in banks)

print("cycles: {}".format(len(states)))
