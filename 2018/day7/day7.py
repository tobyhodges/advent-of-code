#! /usr/bin/env python

from sys import argv, stdout

def process_lines():
    nodes = {}
    seen = []
    with open(argv[1], 'r') as fh:
        for line in fh.readlines():
            fields = line.split()
            current_step = fields[7]
            depends_on   = fields[1]
            if current_step in nodes:
                nodes[current_step].append(depends_on)
            else:
                nodes[current_step] = [depends_on]
            seen.append(current_step)
            seen.append(depends_on)
    seen = set(seen)
    for letter in seen:
        if letter not in nodes:
            nodes[letter] = []
    return nodes

def day7part1(nodes):
    order = ''
    while nodes:
        doable = [ node for node in nodes if not nodes[node] ]
        next = sorted(doable)[0]
        order += next
        for node in nodes:
            if next in nodes[node]:
                nodes[node].remove(next)
        del nodes[next]
    return order

def process_node(node, workers_nodes, workers_times):
    _alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    node_seconds = _alphabet.index(node) + 61
    workers_nodes[workers_times.index(0)] = node
    workers_times[workers_times.index(0)] = node_seconds
    return (workers_nodes, workers_times)

def run_down_clock(total, workers_nodes, workers_times):
    _next_to_finish = workers_times.index(min([x for x in workers_times if x > 0]))
    rundown = workers_times[_next_to_finish]
    workers_times = [ max(0, x - rundown) for x in workers_times ]
    total += rundown
    return (total, workers_nodes, workers_times)

def remove_node(workers_nodes, workers_times):
    if 0 in workers_times:
        if workers_nodes[workers_times.index(0)]:
            done = workers_nodes[workers_times.index(0)]
            workers_times.remove(0)
            workers_nodes.remove(done)
            workers_times.append(0)
            workers_nodes.append('')
            return done, workers_nodes, workers_times
        else:
            raise ValueError('error: nothing to remove')
    else:
        raise ValueError('error: nothing to remove')

def cleanup_nodes(nodes, done):
    for node in nodes:
        if done in nodes[node]:
            nodes[node].remove(done)
    del nodes[done]
    return nodes

def prioritise(doable, workers_nodes):
    output = doable[:]
    for n in doable:
        if n in workers_nodes:
            output.remove(n)
            output += [n]
    return output

def day7part2(nodes):
    order = ''
    total = 0
    workers_times = [0,0,0,0,0]
    workers_nodes = ['','','','','']
    while nodes:
        doable = [ node for node in nodes if not nodes[node] ]
        doable.sort()
        doable = prioritise(doable, workers_nodes)
        for l in doable:
            if l not in workers_nodes:
                if 0 in workers_times:
                    workers_nodes, workers_times = process_node(l, workers_nodes, workers_times)
                else:
                    total, workers_nodes, workers_times = run_down_clock(total, workers_nodes, workers_times)
                    done, workers_nodes, workers_times = remove_node(workers_nodes, workers_times)
                    nodes = cleanup_nodes(nodes, done)
                    break
            else:
                total, workers_nodes, workers_times = run_down_clock(total, workers_nodes, workers_times)
                done, workers_nodes, workers_times = remove_node(workers_nodes, workers_times)
                nodes = cleanup_nodes(nodes, done)
                break
    return total

if __name__ == '__main__':
    nodes = process_lines()
    stdout.write(f"Part 1:\n{day7part1(nodes)}\n")
    nodes = process_lines()
    stdout.write(f"Part 2:\n{day7part2(nodes)}\n")
