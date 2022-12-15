from argparse import ArgumentParser
from ast import literal_eval


def compare_packets(pkt1, pkt2):
    if type(pkt1) == list:
        if type(pkt2) == list:
            if pkt1 == pkt2:
                return "="
            if not pkt1:
                # print("left packet ran out")
                return True
            if not pkt2:
                # print("right packet ran out")
                return False
            while pkt2:
                if not pkt1:
                    # print("left packet ran out")
                    return True
                x = pkt1.pop(0)
                y = pkt2.pop(0)
                z = compare_packets(x, y)
                if z == "=":
                    continue
                return z
            if pkt1:
                # print("right packet ran out")
                return False
            return "="
        return compare_packets(pkt1, [pkt2])
    if type(pkt2) == list:
        return compare_packets([pkt1], pkt2)
    if pkt1 < pkt2:
        return True
    if pkt1 > pkt2:
        return False
    return "="


def part1(infile):
    good_packets = 0
    pair = 0
    with open(infile, "r") as f:
        for row in f:
            if row.strip() == "":
                continue
            pair += 1
            x, y = literal_eval(row.strip()), literal_eval(next(f).strip())
            if compare_packets(x, y) is True:
                good_packets += pair
    return good_packets


def main():
    if args.p == 1:
        print(part1(args.f))
    else:
        raise NotImplementedError("Solution for this part not yet implemented")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
