#! /usr/bin/env python

from sys import argv, stdout
import numpy as np

class Claim:
    '''A simple object to carry the info for each claim.'''
    def __init__(self, num, x, y, w, h):
        self.num    = int(num)
        self.x      = int(x)
        self.y      = int(y)
        self.width  = int(w)
        self.height = int(h)

def read_claims():
    '''Read in the input file and return a list of Claim objects, as well as
    the maximum x- and y-coordinates to give the dimensions of the grid.'''
    max_x = 0
    max_y = 0
    claims = []
    with open(argv[1], 'r') as fh:
        for line in fh.readlines():
            num, _, xy, dims = line.strip().split()
            num = num.strip('#')
            x, y = xy.strip(':').split(',')
            width, height = dims.split('x')
            x = int(x)
            y = int(y)
            width = int(width)
            height = int(height)
            claims.append(Claim(num, x, y, width, height))
            max_x = max(max_x, x+width)
            max_y = max(max_y, y+height)
    return (claims, max_x, max_y)

def day3part1(claims, max_x, max_y):
    '''Create a grid of numbers showing to how many claims each
    position belongs.'''
    grid = np.zeros([max_x, max_y])
    for c in claims:
        grid[c.x:c.x+c.width,c.y:c.y+c.height] += 1
    return grid

def day3part2(filled_grid, claims):
    '''Find the claim whose filled grid section contains only 1s.'''
    for c in claims:
        if np.all(filled_grid[c.x:c.x+c.width,c.y:c.y+c.height] == np.ones([c.width,c.height])):
            return c.num

# part 1
claims, max_x, max_y = read_claims()
filled_grid = day3part1(claims, max_x, max_y)
stdout.write(f"{(sum(sum(filled_grid>1)))}\n")

# part 2
claim_id = day3part2(filled_grid, claims)
stdout.write(f"{claim_id}\n")
