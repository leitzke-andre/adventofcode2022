# aoc_template.py

import pathlib
import sys

guide = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

def get_match_result_part1(round):
    match round[2]:
        case 'X':
            if round[0] == 'A':
                return 3
            elif round[0] == 'B':
                return 0
            else:
                return 6
        case 'Y':
            if round[0] == 'A':
                return 6
            elif round[0] == 'B':
                return 3
            else:
                return 0
        case 'Z':
            if round[0] == 'A':
                return 0
            elif round[0] == 'B':
                return 6
            else:
                return 3

def get_match_result_part2(projected_result):
    match projected_result:
        case 'X':
            #lose
            return 0
        case 'Y':
            #draw
            return 3
        case 'Z':
            #win
            return 6

def get_selection_score(selection):
    match selection:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
        case _:
            return 0

def get_selection_score_part2(round):
   match round[2]:
        case 'X': #lose
            if round[0] == 'A': #opponent picks rock
                return 3
            elif round[0] == 'B': #opponent picks paper
                return 1
            else: #opponent picks scissors
                return 2
        case 'Y': #draw
            if round[0] == 'A': #opponent picks rock
                return 1
            elif round[0] == 'B': #opponent picks paper
                return 2
            else: #opponent picks scissors
                return 3
        case 'Z': #win
            if round[0] == 'A': #opponent picks rock
                return 2
            elif round[0] == 'B': #opponent picks paper
                return 3
            else: #opponent picks scissors
                return 1
    

def calculate_score_part1(round):
    score = 0
    score += get_match_result_part1(round)
    score += get_selection_score(round[2])
    return score

def calculate_score_part2(round):
    score = 0
    score += get_match_result_part2(round[2])
    score += get_selection_score_part2(round)
    return score 


def parse(puzzle_input):
    return puzzle_input

def part1(data):
    total_score = 0
    for line in data:
        total_score += calculate_score_part1(list(line))
    return total_score

def part2(data):
    total_score = 0
    for line in data:
        total_score += calculate_score_part2(list(line))
    return total_score

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data.seek(0)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = open(path, 'r')
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))