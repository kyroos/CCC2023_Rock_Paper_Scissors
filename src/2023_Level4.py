# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 4

import sys

R = P = S = 0

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


def winner(tournament):
    while len(tournament) >= 2:
        tournament = "".join(fight(pair) for pair in zip(tournament[::2], tournament[1::2]))
    return tournament


def solve(count):
    global R, P, S
    if P == 0 or R == 0:
        ret = "P" * P + "R" * R + "S" * S
        R = S = P = 0
    elif R >= count - 1 and P >= 1:
        # eliminate as many rocks as possible
        R -= count - 1
        P -= 1
        ret = "R" * (count - 1) + "P"
    else:
        left = solve(count // 2)
        right = solve(count // 2)
        ret = left + right
    return ret


def main(file_name):
    global R, P, S
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    N, M = map(int, lines.pop(0).split())
    for line in lines:
        R, P, S = [int(x[:-1]) for x in line.split()]
        ans = solve(M)
        assert winner(ans) == "S" and len(ans) == M
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level4.py <file_name>")

