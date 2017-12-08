#! /usr/bin/env python

from sys import argv

# part 1

def is_valid(string):
    words = string.strip().split()
    deduped = set(words)
    return len(words) == len(deduped)

# part 2

def is_valid_angram(string):
    words = string.strip().split()
    sorted_letters = [''.join(sorted(list(x))) for x in words]
    return len(words) == len(set(sorted_letters))

inputfile = argv[1]
counter = 0
with open(inputfile, 'r') as fh:
    for line in fh.readlines():
        if is_valid_angram(line):
            counter += 1

print(counter)
