# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 1

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


def solve(pair):
    return fight(pair)


def main(file_name):
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    N = int(lines.pop(0))
    for pair in lines:
        ans = solve(pair)
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level1.py <file_name>")
