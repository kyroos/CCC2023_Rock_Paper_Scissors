# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 3

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


def solve(R, P, S):
    ans = ""
    while R >= 3 and P >= 1:
        ans += "RRRP"
        R -= 3
        P -= 1

    while R >= 1 and P >= 1:
        ans += "RP"
        R -= 1
        P -= 1

    assert R <= 1

    if R == 1:
        assert S >= 1
        ans += "RS"
        R -= 1
        S -= 1

    ans += "P" * P + "S" * S

    assert do_two_rounds(ans).count("R") == 0
    assert do_two_rounds(ans).count("S") >= 1

    return ans


def main(file_name):
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    N, M = map(int, lines.pop(0).split())
    for line in lines:
        R, P, S = [int(x[:-1]) for x in line.split()]
        ans = solve(R, P, S)
        assert len(ans) == M
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level3.py <file_name>")
