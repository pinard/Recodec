#!/usr/bin/env python
# Copyright © 1999, 2000, 2001, 2002 Progiciels Bourbeau-Pinard inc.
# François Pinard <pinard@iro.umontreal.ca>, 1999.

"""\
A graph is made from a set of vertices, and a set of oriented arcs.

Each vertex should be immutable and not None.  An arc is a tuple.  The first
and second element of an arc are mandatory, and represent the starting
vertex and ending vertex for that arc.  The optional third element of an
arc is its associate positive cost, a cost of one is implied if none given.
"""

def path(before, after, arcs):
    """\
Return the most economical path from the BEFORE vertex to the AFTER vertex,
given a set of ARCS representing possible partial paths.  The path is
returned as a list of successive arcs connecting BEFORE to AFTER, or None
is there is no such path.
"""
    # With each vertex, associate a best forward arc and total cost.
    table = {after: (None, 0)}
    changed = True
    while changed:
        changed = False
        for arc in arcs:
            entry = table.get(arc[1])
            if entry is not None:
                if len(arc) < 3:
                    cost = 1 + entry[1]
                else:
                    cost = arc[2] + entry[1]
                previous = table.get(arc[0])
                if previous is None or cost < previous[1]:
                    table[arc[0]] = arc, cost
                    changed = True
    # Rebuild best path.
    entry = table.get(before)
    if entry is None:
        return None
    path = []
    arc = entry[0]
    while arc is not None:
        path.append(arc)
        arc = table[arc[1]][0]
    return path

def sort(vertices, arcs):
    """\
Topologically sort VERTICES, while obeying the constraints described
in ARCS.  Arcs referring to non-listed vertices are ignored.  Return two
lists, which together hold all original VERTICES, with none repeated.
The first list is the sorted result, the second list gives all vertices
involved into some cycle.
"""
    # With each vertex, associate a predecessor count and the set of all
    # follower vertices.
    table = {}
    for vertex in vertices:
        table[vertex] = [vertex, 0, []]
    for arc in arcs:
        before = table.get(arc[0])
        after = table.get(arc[1])
        if before is not None and after is not None and after not in before[2]:
            before[2].append(after)
            after[1] += 1
    vertices = table.values()
    del table
    # Accumulate sorted vertices in the SORTED list.
    zeroes = []
    for vertex in vertices[:]:
        if vertex[1] == 0:
            vertices.remove(vertex)
            zeroes.append(vertex)
    sorted = []
    while zeroes:
        new_zeroes = []
        zeroes.sort()
        for zero in zeroes:
            sorted.append(zero[0])
            for vertex in zero[2]:
                vertex[1] -= 1
                if vertex[1] == 0:
                    vertices.remove(vertex)
                    new_zeroes.append(vertex)
        zeroes = new_zeroes
    # Unprocessed vertices participate into various cycles.
    cycles = []
    for vertex in vertices:
        cycles.append(vertex[0])
        del vertex[2]
    return sorted, cycles
