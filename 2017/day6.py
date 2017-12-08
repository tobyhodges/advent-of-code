#! /usr/bin/python

from sys import argv

def reallocate_blocks(input_list):
    max_pos = input_list.index(max(input_list))
    max_blocks = input_list[max_pos]
    input_list[max_pos] = 0
    index = max_pos
    blocks = max_blocks
    while blocks > 0:
        index += 1
        if index == len(input_list):
            index = 0
        input_list[index] += 1
        blocks -= 1
    current_state = ''.join([str(x) for x in input_list])
    return current_state, input_list

inp = '0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11'
inp = [int(x) for x in inp.split()]
seen_states = []
last_seen = 'whatevs'
steps = 0

# part 1
# while True:
#     steps += 1
#     last_seen, inp = reallocate_blocks(inp)
#     if last_seen not in seen_states:
#         seen_states.append(last_seen)
#     else:
#         break
# print(steps)

while True:
    last_seen, inp = reallocate_blocks(inp)
    if last_seen not in seen_states:
        seen_states.append(last_seen)
    else:
        print(len(seen_states[seen_states.index(last_seen):]))
        break
