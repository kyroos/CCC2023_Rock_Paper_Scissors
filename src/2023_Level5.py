# 37th Classic CCC The Web ONLINE
# Rock, Paper, Scissors
# Level 5

import sys
import math

R = P = S = Y = L = 0

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


def solve(count):
    global R, P, S, Y, L

    if P == 0 and L == 0:
        ret = "R" * R + "Y" * Y + "S" * S
        R = Y = S = 0

    elif R + Y >= count - 1 and P >= 1:
        RR = min(R, count - 1)
        YY = count - 1 - RR
        R -= RR
        Y -= YY
        P -= 1
        ret = "R" * RR + "Y" * YY + "P"

    elif R == 0 and Y + L >= count and L >= 1:
        YY = min(Y, count - 1)
        LL = count - YY
        Y -= YY
        L -= LL
        ret = "Y" * YY + "L" * LL

    elif count >= 4 and R >= 1 and R + Y >= count - 1 and Y >= int(math.log(count, 2)) and L >= 1:

        """
        If there is no 'P' available to eliminate all the 'R's, look for this pattern to guarantee a win for 'L'
        
                                                                                        R  Y  L  count
            YRYL                                                                        1  2  1      4
            YRRRYRYL                                                                    4  3  1      8
            YRRRRRRRYRRRYRYL                                                           11  4  1     16
            YRRRRRRRRRRRRRRRYRRRRRRRYRRRYRYL                                           26  5  1     32 
            YRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRYRRRRRRRRRRRRRRRYRRRRRRRYRRRYRYL           57  6  1     64
            ...
        """

        ret = "YRYL"
        ct = 4
        R -= 1
        L -= 1
        Y -= 2
        while ct < count:
            RR = min(ct - 1, R)
            YY = ct - RR
            R -= RR
            Y -= YY
            ret += "Y" * YY + "R" * RR
            ct *= 2

    else:
        left = solve(count // 2)
        right = solve(count // 2)
        ret = left + right

    return ret


def main(file_name):
    global R, P, S, Y, L
    with open(f"{file_name}") as f:
        lines = f.read().strip().split('\n')

    N, M = map(int, lines.pop(0).split())
    for line in lines:
        R, P, S, Y, L = [int(x[:-1]) for x in line.split()]
        ans = solve(M)
        assert len(ans) == M and winner(ans) == "S"
        print(ans)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Usage: python level5.py <file_name>")
