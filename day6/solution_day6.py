# aoc_template.py

import pathlib
import sys

from collections import deque

def parse(puzzle_input):
    return puzzle_input.read()

def part1(data):
    initial_pos = 4
    d = deque(data[:4]) #preinitialize deque with first 4 characters
    for i in range(initial_pos, len(data)):
        if len(set(d)) == 4:
            return i
        d.popleft()
        d.append(data[i])
    return "Error"

def part2(data):
    initial_pos = 14
    d = deque(data[:14]) #preinitialize deque with first 4 characters
    for i in range(initial_pos, len(data)):
        if len(set(d)) == 14:
            return i
        d.popleft()
        d.append(data[i])
    return "Error"

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