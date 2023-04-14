# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 2

import sys

rules = {
    "PP": "P",
    "RR": "R",
    "SS": "S",
    "PS": "S", "SP": "S",
    "PR": "P", "RP": "P",
    "RS": "R", "SR": "R"
}


def fight(pair):
    return rules["".join(pair)]


def do_two_rounds(fights):
    for _ in range(2):
        fights = "".join(fight(pair) for pair in zip(fights[::2], fights[1::2]))
    return fights


def solve(tour):
    return do_two_rounds(tour)


def main(file_name):
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    N, M = map(int, lines.pop(0).split())
    for line in lines:
        ans = solve(line)
        assert len(ans) == M // 4
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level2.py <file_name>")
