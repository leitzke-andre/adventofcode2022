# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    elf_pairs = []
    for line in puzzle_input:
        sorted_elfs = []
        elfs = line.split(',')
        for elf in elfs:
            section_ids = elf.split('-') 
            sections = []
            sections.append(int(section_ids[0]))
            sections.append(int(section_ids[1]))
            sorted_elfs.append(sections)
        elf_pairs.append(sorted_elfs)
    return elf_pairs

def check_fully_contained(elf_pair):
    if (
        ((elf_pair[0][0] >= elf_pair[1][0]) and (elf_pair[0][1] <= elf_pair[1][1])) or 
        ((elf_pair[1][0] >= elf_pair[0][0]) and (elf_pair[1][1] <= elf_pair[0][1]))
        ):
        return 1
    return 0

def check_partially_contained(elf_pair):
    if (
        (elf_pair[0][0] >= elf_pair[1][0] >= elf_pair[0][1]) or 
        (elf_pair[1][0] >= elf_pair[0][0] >= elf_pair[1][1]) or
        (elf_pair[0][0] <= elf_pair[1][1] <= elf_pair[0][1]) or 
        (elf_pair[1][0] <= elf_pair[0][1] <= elf_pair[1][1])
        ):
        return 1
    return 0

def part1(data):
    """Solve part 1."""
    contained_sections = 0
    for elf_pair in data:
        contained_sections += check_fully_contained(elf_pair)
    return contained_sections

def part2(data):
    """Solve part 2."""
    contained_sections = 0
    for elf_pair in data:
        contained_sections += check_partially_contained(elf_pair)
    return contained_sections

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