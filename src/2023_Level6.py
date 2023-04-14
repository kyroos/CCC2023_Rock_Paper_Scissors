# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 6

import sys
import random

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
    "RS": "R", "SR": "R"
}


def fight(pair):
    return rules["".join(pair)]


def winner(tournament):
    while len(tournament) >= 2:
        tournament = "".join(fight(pair) for pair in zip(tournament[::2], tournament[1::2]))
    return tournament


def random_fill(tournament):
    choices = ['P', 'S', 'L', 'Y', 'R']
    return ''.join(random.choice(choices) if c == 'X' else c for c in tournament)


def solve(tournament):
    while True:
        rnd_tour = random_fill(tournament)
        if winner(rnd_tour) == 'S':
            return rnd_tour


def main(file_name):
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    N, M = map(int, lines.pop(0).split())
    for line in lines:
        ans = solve(line)
        assert winner(ans) == "S"
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level6.py <file_name>")
