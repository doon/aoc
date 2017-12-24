#!/usr/bin/env python3

file = open("../input/input.txt","r")
f = file.read()
f = f.strip()
l = len(f)
offset = int(l/2)
s = 0
for x in range(0,l):
    n = x + offset
    if n >= l:
        n = n - l

    if f[x] == f[n]:
        s += int(f[x])
print(s)
