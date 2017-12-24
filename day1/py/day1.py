#!/usr/bin/env python3

file = open("../input/input.txt","r")
f = file.read()
f = f.strip()
l = len(f)
s = 0
for x in range(0,l):
    print("looking at ",x)
    if x == l-1:
        if f[x] == f[0]:
            s += int(f[x])
    else:
        if f[x] == f[x+1]:
            s += int(f[x])
print(s)
