"""
--- Part Two ---

For some reason, your simulated results don't match what the experimental energy source engineers expected.
Apparently, the pocket dimension actually has four spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer 4-dimensional coordinate (x,y,z,w),
there exists a single cube (really, a hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any of their coordinates differ by at
most 1. For example, given the cube at x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3,
the cube at x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region of cubes. Furthermore, the same rules
for cycle updating still apply: during each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even though the pocket dimension is
4-dimensional, this initial state represents a small 2-dimensional slice of it. (In particular, this initial state
defines a 3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following configurations, where the result of each cycle
is shown layer-by-layer at each given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....

After the full six-cycle boot process completes, 848 cubes are left in the active state.

Starting with your given initial configuration, simulate six cycles in a 4-dimensional space. How many cubes are left
in the active state after the sixth cycle? """

with open("input.txt") as input_file:
    # initial_plane is a list of the rows
    initial_plane = input_file.read().strip().split("\n")

active_cubes = []  # Stores the active cubes in the form of tuples (x, y, z, w)
active_neighbors = {}  # stores the number of active neighbors of a cube


def get_neighbor_coords(n_pos):
    # Return list of coordinate tuples of all surrounding cubes
    n = []
    for nx in [-1, 0, 1]:
        for ny in [-1, 0, 1]:
            for nz in [-1, 0, 1]:
                for nw in [-1, 0, 1]:
                    if not (nx == ny == nz == nw == 0):
                        coords = (n_pos[0] + nx, n_pos[1] + ny, n_pos[2] + nz, n_pos[3] + nw)
                        n.append(coords)
    return n


# Initialize active_cubes and active_neighbors
for i, row in enumerate(initial_plane):
    for j, element in enumerate(row):
        if element == "#":
            pos = (i, j, 0, 0)
            active_cubes.append(pos)
            active_neighbors[pos] = 0
# Initialize active_neighbors
for pos in active_cubes:
    neighbors = get_neighbor_coords(pos)
    for nbr in neighbors:
        if nbr in active_neighbors.keys():
            active_neighbors[nbr] += 1
        else:
            active_neighbors[nbr] = 1
# Perform 6 iterations
for _ in range(6):
    last_active = active_cubes.copy()
    last_neighbors = active_neighbors.copy()

    for position in last_neighbors.keys():

        if position in last_active and not (1 < last_neighbors[position] < 4):
            active_cubes.remove(position)
            for neighbor in get_neighbor_coords(position):
                active_neighbors[neighbor] -= 1

        elif position not in last_active and last_neighbors[position] == 3:
            active_cubes.append(position)
            for neighbor in get_neighbor_coords(position):
                if neighbor in active_neighbors.keys():
                    active_neighbors[neighbor] += 1
                else:
                    active_neighbors[neighbor] = 1


print("Remaining active cubes: {}".format(len(active_cubes)))