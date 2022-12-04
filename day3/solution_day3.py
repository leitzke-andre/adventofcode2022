# aoc_template.py

import pathlib
import sys

def get_prio_from_char(character):
    #convert the entire input in a list of character codes.
    #extract the priority from each by subtraction 
    #if the character is outside the range for roman characters, ignore by assigning None
    charcode = ord(character)
    prio = 0
    if (charcode > 96 and charcode < 123):
        prio = charcode - 96
    elif (charcode > 64 and charcode < 91):
        prio = charcode - 38
    else:
        prio = None
    return prio

def parse(puzzle_input):
    """Parse input."""
    #returns a list of rucksacks with the prio for each item
    list = []
    for line in puzzle_input:
        rucksack = []
        for character in line:
            prio = get_prio_from_char(character)
            if prio is not None:
                rucksack.append(prio)
        else:
            list.append(rucksack)
    return list


def part1(data):
    """Solve part 1."""
    sum = 0
    for line in data:
        found = False
        midpoint = len(line)//2
        line_part_1 = line[:midpoint]
        line_part_2 = line[midpoint:]
        for item in line_part_1:
            if (item in line_part_2):
                sum += item
                found = True
            if found:
                break
    return sum

def part2(data):
    """Solve part 2."""
    return "TBD"

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
