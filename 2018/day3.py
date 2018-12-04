#! /usr/bin/env python

from sys import argv, stdout
import numpy as np

class Claim:
    def __init__(self, num, x, y, w, h):
        self.num    = int(num)
        self.x      = int(x)
        self.y      = int(y)
        self.width  = int(w)
        self.height = int(h)

def day3part1():
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

    grid = np.zeros([max_x, max_y])
    for c in claims:
        grid[c.x:c.x+c.width,c.y:c.y+c.height] += 1
    return grid

# filled_grid = day3part1()
# stdout.write(f"{(sum(sum(filled_grid>1)))}\n")

def day3part2():
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

    grid = np.zeros([max_x, max_y])
    for c in claims:
        grid[c.x:c.x+c.width,c.y:c.y+c.height] += 1
    for c in claims:
        if np.all(grid[c.x:c.x+c.width,c.y:c.y+c.height] == np.ones([c.width,c.height])):
            return c.num

claim_id = day3part2()
stdout.write(f"{claim_id}\n")
