#!/usr/bin/env python

def read_input(filename):
    with open(filename, 'r') as infh:
        return infh.readline().strip().split('-')

def check_twins(number):
    return len(str(number)) != len(set(str(number)))

def check_ascending(number):
    return number == int(''.join(sorted(str(number))))

def find_potential_passwords(start, end):
    num_potential_passwords = 0
    for i in range(start, end+1):
        if check_twins(i) and check_ascending(i):
            num_potential_passwords += 1
    return num_potential_passwords

def check_groups(number):
    num_pairs = 0
    for c in set(str(number)):
        num_pairs += str(number).count(c) == 2
    return num_pairs

def find_potential_passwords_part2(start, end):
    num_potential_passwords = 0
    for i in range(start, end+1):
        if check_twins(i) and check_ascending(i):
            if check_groups(i):
                num_potential_passwords += 1
    return num_potential_passwords

start, end = read_input('day4.txt')
print(find_potential_passwords(int(start), int(end)))
print(find_potential_passwords_part2(int(start), int(end)))
