#! /usr/bin/env python

from sys import stdout, argv
import re
import datetime
import numpy as np

def getLineList():
    with open(argv[1], 'r') as fh:
        lines = fh.readlines()
        lines =[ l.strip() for l in lines ]
    return lines

def get_nap_data(list_of_lines):
    naps = {}
    for line in list_of_lines:
        search = re.match(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] ([A-Za-z0-9 #]+)', line)
        date_time, activity = search.groups()
        if "Guard" in activity:
            search = re.search(r'#\d+', activity)
            guard_num = search.group(0)
            current_guard = guard_num
        if "falls" in activity:
            started_sleeping = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
        if "wakes" in activity:
            woke_up = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M')
            time_asleep = woke_up - started_sleeping
            if current_guard not in naps:
                naps[current_guard] = [(started_sleeping, woke_up, time_asleep)]
            else:
                naps[current_guard].append((started_sleeping, woke_up, time_asleep))
    if current_guard not in naps:
        naps[current_guard] = [(started_sleeping, woke_up, time_asleep)]
    else:
        naps[current_guard].append((started_sleeping, woke_up, time_asleep))
    return naps

def create_napgrid(naps):
    nap_grid = np.zeros([len(naps), 60])
    guards = []
    for i, guard in enumerate(naps):
        guards.append(guard)
        for start, end, total in naps[guard]:
            nap_grid[i,start.minute:end.minute] += 1
    return nap_grid, guards

def day4part1(nap_grid, guards):
    total_asleep = list([sum(r) for r in nap_grid])
    max_guard = guards[total_asleep.index(max(total_asleep))]
    max_row = guards.index(max_guard)
    max_guard_naps = nap_grid[max_row]
    max_minute = int(np.where(max_guard_naps == max(max_guard_naps))[0])
    return int(max_guard.lstrip('#')) * max_minute

def day4part2(nap_grid, guards):
    max_coords = np.where(nap_grid == np.max(nap_grid))
    row = int(max_coords[0])
    col = int(max_coords[1])
    return int(guards[row].lstrip('#')) * col


unsorted_lines = getLineList()
sorted_lines = sorted(unsorted_lines)
naps = get_nap_data(sorted_lines)

stdout.write(f"Part 1:\n{day4part1(*create_napgrid(naps))}\n")
stdout.write(f"Part 2:\n{day4part2(*create_napgrid(naps))}\n")
