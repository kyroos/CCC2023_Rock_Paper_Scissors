# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 7

import sys
import random
from functools import cache

rules = {
    "PP": "P",
    "RR": "R",
    "SS": "S",
    "LL": "L",
    "YY": "Y",
    "PS": "S", "SP": "S",
    "PR": "P", "RP": "P",
    "RL": "R", "LR": "R",
    "LY": "L", "YL": "L",
    "SY": "Y", "YS": "Y",
    "SL": "S", "LS": "S",
    "PL": "L", "LP": "L",
    "PY": "P", "YP": "P",
    "RY": "Y", "YR": "Y",
    "RS": "R", "SR": "R",
    "ZZ": "RPSLY",
    "ZR": "RPY", "RZ": "RPY",
    "ZP": "PLS", "PZ": "PLS",
    "ZS": "SRY", "SZ": "SRY",
    "ZL": "LRS", "LZ": "LRS",
    "ZY": "YPL", "YZ": "YPL"
}

@cache
def multi_winner(left, right):
    seen = {rules[l + r] for l in left for r in right}
    return ''.join(seen)


@cache
def winner(tour):
    if len(tour) == 2:
        return rules[tour]

    left = winner(tour[0:len(tour) // 2])
    right = winner(tour[len(tour) // 2:])

    return multi_winner(left, right)


def random_fill(tournament, choices):
    return ''.join(random.choice(choices) if c == 'X' else c for c in tournament)


def solve(tournament):
    while True:
        for choice in (['P', 'S', 'L'], ['P', 'S', 'L', 'Y', 'R']):
            rnd_tour = random_fill(tournament, choice)
            if winner(rnd_tour) == 'S':
                return rnd_tour


def main(file_name):
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    random.seed(2023)
    N, M = map(int, lines.pop(0).split())
    for line in lines:
        ans = solve(line)
        assert winner(ans) == 'S'
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level7.py <file_name>")
        main("level7\\level7_1.in")
