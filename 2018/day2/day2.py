#! /usr/bin/env python

from sys import argv, stdout
from collections import Counter

##############################################################################
# Part 1
##############################################################################

def day2part1():
    twos = []
    threes = []
    with open(argv[1], 'r') as fh:
        for line in fh.readlines():
            line = line.strip()
            counts = Counter(line)
            if 2 in counts.values():
                twos.append(line)
            if 3 in counts.values():
                threes.append(line)
    stdout.write(f"{len(twos) * len(threes)}")

##############################################################################
# Part 2
##############################################################################

def getDistance(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

def day2part2():
    with open(argv[1], 'r') as fh:
        lines = [line.strip() for line in fh.readlines()]
        for l in lines:
            for m in lines:
                if l != m:
                    dist = getDistance(l, m)
                    if dist == 1:
                        return f"{''.join([l[i] for i in range(len(l)) if l[i] == m[i]])}"


stdout.write(f"{day2part2()}\n")
