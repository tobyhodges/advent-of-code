#! /usr/bin/env python

from sys import argv, stdout

##############################################################################
# Part 1
##############################################################################

def day1part1():
    frequency = 0
    with open(argv[1], 'r') as fh:
        for line in fh.readlines():
            frequency += int(line)
    stdout.write(f"{frequency}\n")

##############################################################################
# Part 2
##############################################################################

def process_frequencies(numbers, frequency, seen):
    for line in numbers:
        line = line.strip()
        frequency += int(line)
        if frequency not in seen:
            seen.add(frequency)
        else:
            stdout.write(f"{frequency}\n")
            frequency = 'done'
            break
    return (frequency, seen)

def day1part2():
    frequency = 0
    seen = set([0])
    with open(argv[1], 'r') as fh:
        lines = fh.readlines()
        switch = ''
        while frequency != 'done':
            frequency, seen = process_frequencies(lines, frequency, seen)

day1part2()
