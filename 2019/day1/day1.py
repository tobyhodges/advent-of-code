#!/usr/bin/env python

def calculate_fuel(mass):
    return int(int(mass) / 3) - 2

def fuel_for_module(mass):
    fuel_needed = 0
    while True:
        mass = calculate_fuel(mass)
        fuel_needed += mass
        if calculate_fuel(mass) < 1:
            return fuel_needed

# part 1
fuel_needed = 0
with open('day1.txt', 'r') as infh:
    for line in infh.readlines():
        fuel_needed += calculate_fuel(line.strip())
    print(fuel_needed)

# part 2
fuel_needed = 0
with open('day1.txt', 'r') as infh:
    for line in infh.readlines():
        fuel_needed += fuel_for_module(line.strip())
    print(fuel_needed)
