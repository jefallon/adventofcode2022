import argparse


def part1(infile):
    score = 0
    with open(infile, "r") as f:
        for row in f:
            opp, you = row.strip().split()
            score += play(opp, you)
    return score


def part2(infile):
    score = 0
    with open(infile, "r") as f:
        for row in f:
            opp, you = row.strip().split()
            score += force(opp, you)
    return score


def force(opponent, outcome):
    strat_val = {"X": 1, "Y": 2, "Z": 3}
    win = {"A": "Y", "B": "Z", "C": "X"}
    tie = {"A": "X", "B": "Y", "C": "Z"}
    lose = {"A": "Z", "B": "X", "C": "Y"}
    if outcome == "X":
        return strat_val[lose[opponent]]
    if outcome == "Y":
        return 3 + strat_val[tie[opponent]]
    return 6 + strat_val[win[opponent]]


def play(opponent, player):
    wins = {"Z": "B", "Y": "A", "X": "C"}
    strat_val = {"X": 1, "Y": 2, "Z": 3}
    if opponent == wins[player]:
        return strat_val[player] + 6
    if ord(opponent) + 23 == ord(player):
        return strat_val[player] + 3
    return strat_val[player]


def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError("Solution for that part is not yet implemented")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
