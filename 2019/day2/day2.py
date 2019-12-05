#!/usr/bin/env python

def read_input(filename):
    with open(filename, 'r') as infh:
        intcode = [ int(x) for x in infh.readline().split(',')]
    return intcode

def intcode_computer(intcode, stepsize=4):
    for i in range(0, len(intcode), stepsize):
        program = intcode[i]
        if program == 99:
            return intcode
        elif program not in (1, 2):
            raise ValueError('Invalid program code:', program)
        else:
            parameters = intcode[i+1:i+stepsize]
            v1  = intcode[intcode[i+1]]
            v2  = intcode[intcode[i+2]]
            out = parameters[-1]
            if program == 1:
                intcode[out] = v1 + v2
            elif program == 2:
                intcode[out] = v1 * v2

# part 1
intcode = read_input('day2.txt')
intcode[1] = 12
intcode[2] = 2
intcode = intcode_computer(intcode)
print(intcode[0])

# part 2
# part 2
for noun in range(100):
    for verb in range(100):
        intcode = read_input('day2.txt')
        intcode[1] = noun
        intcode[2] = verb
        if intcode_computer(intcode)[0] == 19690720:
            print(100 * noun + verb)
