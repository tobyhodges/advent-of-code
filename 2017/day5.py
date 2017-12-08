#! /usr/bin/env python

from sys import argv

# part 1
def traverse_maze(sequence):
    steps = 0
    pos = 0
    while pos < len(sequence):
        next_pos = pos + sequence[pos]
        sequence[pos] += 1
        steps += 1
        pos = next_pos
    return steps

# part 2
def traverse_maze_strange(sequence):
    steps = 0
    pos = 0
    while pos < len(sequence):
        next_pos = pos + sequence[pos]
        if sequence[pos] >= 3:
            sequence[pos] -= 1
        else:
            sequence[pos] += 1
        steps += 1
        pos = next_pos
    return steps

input_file = argv[1]
seq = []
with open(input_file, 'r') as fh:
    for line in fh.readlines():
        seq.append(int(line.strip()))
num_steps = traverse_maze_strange(seq)
print(num_steps)
