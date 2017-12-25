#!/usr/bin/env python3

from collections import defaultdict

REGISTERS = defaultdict(lambda: 0)
HIGHEST = 0

with open("../input/input.txt") as file:
    for line in file:
        (register, operation, value, _, condreg, cond, condvalue) = line.strip().split()
        conditional = "REGISTERS['{}'] {} {}".format(condreg, cond, condvalue)
        if eval(conditional):
            if operation == 'inc':
                REGISTERS[register] += int(value)
            else:
                REGISTERS[register] -= int(value)
        h = max(REGISTERS.values())
        if h > HIGHEST:
            HIGHEST = h

print(HIGHEST)