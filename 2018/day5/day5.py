#! /usr/bin/env python

from sys import argv, stdout

def remove_pairs(input_string):
    output_string = ''
    skip_next = False
    for i, c in enumerate(input_string):
        if skip_next:
            skip_next = False
            if i == len(input_string)-1:
                return output_string
        else:
            try:
                if c != input_string[i+1]:
                    if c.upper() == input_string[i+1]:
                        skip_next = True
                    elif c.lower() == input_string[i+1]:
                        skip_next = True
                    else:
                        output_string += c
                else:
                    output_string += c
            except IndexError:
                output_string += c
                return output_string

def day5part1():
    with open(argv[1], 'r') as fh:
        for line in fh.readlines():
            input_string = line.strip()
            trigger = True
            while trigger:
                len_before = len(input_string)
                input_string = remove_pairs(input_string)
                len_after = len(input_string)
                if len_before == len_after:
                    trigger = False
            stdout.write(f"{len_after}\n")


def remove_unit(input_string, letter):
    input_string = input_string.replace(letter, '')
    input_string = input_string.replace(letter.upper(), '')
    return input_string

def day5part2():
    with open(argv[1], 'r') as fh:
        for line in fh.readlines():
            original = line.strip()
            for l in list('abcdefghijklmnopqrstuvwxyz'):
                input_string = remove_unit(original, l)
                trigger = True
                while trigger:
                    len_before = len(input_string)
                    input_string = remove_pairs(input_string)
                    len_after = len(input_string)
                    if len_before == len_after:
                        trigger = False
                stdout.write(f"{l}: {len_after}\n")

if __name__ == "__main__":
    stdout.write("Part 1:\n")
    day5part1()
    stdout.write("Part 2:\n")
    day5part2()
