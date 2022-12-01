# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):    
    calories = []
    current_elf_calories = 0
    for number in puzzle_input:
        if number == '\n':
            calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories = current_elf_calories + int(number)
    else:
        #workaround to add the last after EOF, to be improved... maybe...
        calories.append(current_elf_calories)
    return calories
    
def part1(data):
    return sorted(data, reverse=True)[0]

def part2(data):
    sorted_data = sorted(data, reverse=True)
    return (sorted_data[0] + sorted_data[1] + sorted_data[2])

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