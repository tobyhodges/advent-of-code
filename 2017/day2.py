#! /usr/bin/env python

from sys import argv

# part 1

def find_difference(numbers):
    numbers.sort()
    lowest = numbers[0]
    highest = numbers[-1]
    difference = highest - lowest
    return difference

def process_line(line):
    fields = line.strip().split()
    numbers = [ int(x) for x in fields ]
    difference = find_difference(numbers)
    return difference

def process_sheet(input_file):
    differences = []
    with open(input_file, 'r') as fh:
        for line in fh.readlines():
            differences.append(process_line(line))
    return differences

#inputfile = argv[1]
#diffs = process_sheet(inputfile)
#print sum(diffs)

# part 2

def find_dividers(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            x = max(numbers[i], numbers[j])
            y = min(numbers[i], numbers[j])
            if x % y == 0:
                return x / y

def process_line(line):
    fields = line.strip().split()
    numbers = [ int(x) for x in fields ]
    difference = find_dividers(numbers)
    return difference

def process_sheet(input_file):
    differences = []
    with open(input_file, 'r') as fh:
        for line in fh.readlines():
            differences.append(process_line(line))
    return differences

inputfile = argv[1]
divs = process_sheet(inputfile)
print sum(divs)
