# aoc_template.py

import pathlib
import sys

from collections import deque

def parse(puzzle_input):
    return puzzle_input.read()

def get_start_of_packet_marker(data, marker_size):
    initial_pos = marker_size
    d = deque(data[:marker_size]) #preinitialize deque with first 4 characters
    for i in range(initial_pos, len(data)):
        if len(set(d)) == marker_size:
            return i
        d.popleft()
        d.append(data[i])
    return "Error"

def part1(data):
    return get_start_of_packet_marker(data, 4)

def part2(data):
    return get_start_of_packet_marker(data, 14)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = open(path, 'r')
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))