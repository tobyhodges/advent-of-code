#! /usr/bin/env

from sys import argv

def find_matching_digits(code):
    try:
        codelength = len(code)
    except TypeError:
        code = str(code)
        codelength = len(code)
    matched = []
    for i, digit in enumerate(codelength):
        j = i+1
        if j == codelength:
            j = 0
        if digit == code[j]:
            matched.append(int(digit))
    return matched

def find_matching_digits_halfway(code):
    try:
        codelength = len(code)
    except TypeError:
        code = str(code)
        codelength = len(code)
    halflength = codelength/2
    matched = []
    for i, digit in enumerate(codelength):
        j = i+halflength
        if j >= codelength:
            j = j - codelength
        if digit == code[j]:
            matched.append(int(digit))
    return matched

input = argv[1]
matches = find_matching_digits_halfway(input)
summed = sum(matches)
print(summed)
