#! /usr/bin/env python

from sys import argv
from math import sqrt, ceil

# part 1

def get_distance(input_num):
    core_grid_width = int(sqrt(input_num))
    if core_grid_width % 2:
        core_index_pos = ((core_grid_width-1)/2,(core_grid_width-1)/2)
    else:
        core_index_pos = (((core_grid_width-2)/2)+1,(core_grid_width-2)/2)

    rows = core_grid_width
    cols = core_grid_width
    rem = input_num - (core_grid_width**2)
    if rem != 0:
        sides = int(ceil(float(rem) / core_grid_width))
    else:
        sides = 0

    if core_grid_width % 2 == 0:
        if sides == 0:
            index_pos = core_index_pos
            input_pos = (0,0)
        elif sides == 1:
            index_pos = (core_index_pos[0], core_index_pos[1]+1)
            input_pos = (rem-1, 0)
        elif sides == 2:
            index_pos = (core_index_pos[0], core_index_pos[1]+1)
            input_pos = (core_grid_width, rem-core_grid_width-1)
    else:
        if sides == 0:
            index_pos = core_index_pos
            input_pos = (core_grid_width-1,core_grid_width-1)
        elif sides == 1:
            index_pos = (core_index_pos[0], core_index_pos[1])
            input_pos = ((core_grid_width)-rem, core_grid_width)
        elif sides == 2:
            index_pos = (core_index_pos[0]+1, core_index_pos[1])
            input_pos = (0, core_grid_width-(rem-core_grid_width)+1)

    distance = sum([ abs(x-y) for x,y in zip(index_pos, input_pos) ])
    return distance

#input_number = int(argv[1])
#dist get_distance(input_number)
#print(dist)

# part 2

# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
