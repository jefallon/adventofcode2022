import argparse


def part1(infile):
    top_map = []
    loc_S = None
    loc_E = None
    with open(infile, "r") as f:
        line = 0
        for row in f:
            top_map.append([c for c in row.strip()])
            if "S" in top_map[-1]:
                loc_S = (row.index("S"), line)
            if "E" in top_map[-1]:
                loc_E = (row.index("E"), line)
            line += 1
    e_x, e_y = loc_E
    s_x, s_y = loc_S
    top_map[e_y][e_x] = "z"
    top_map[s_y][s_x] = "a"
    height = len(top_map)
    width = len(top_map[0])
    steps_map = [[0 for _ in top_map[0]] for _ in top_map]
    steps_map[e_y][e_x] = 1
    loc = loc_E
    to_visit = []
    x, y = loc
    for i in [-1, 1]:
        a = x + i
        b = y + i
        if (
            0 <= b < height
            and steps_map[b][x] == 0
            and ord(top_map[b][x]) >= ord(top_map[y][x]) - 1
        ):
            steps_map[b][x] = steps_map[y][x] + 1
            to_visit.append((x, b))
        if (
            0 <= a < width
            and steps_map[y][a] == 0
            and ord(top_map[y][a]) >= ord(top_map[y][x]) - 1
        ):
            steps_map[y][a] = steps_map[y][x] + 1
            to_visit.append((a, y))
    # return to_visit
    while to_visit:
        x, y = to_visit.pop(0)
        if (x, y) == loc_S:
            return steps_map[y][x] - 1
        for i in [-1, 1]:
            a = x + i
            b = y + i
            if (
                0 <= b < height
                and steps_map[b][x] == 0
                and ord(top_map[b][x]) >= ord(top_map[y][x]) - 1
            ):
                steps_map[b][x] = steps_map[y][x] + 1
                to_visit.append((x, b))
            if (
                0 <= a < width
                and steps_map[y][a] == 0
                and ord(top_map[y][a]) >= ord(top_map[y][x]) - 1
            ):
                steps_map[y][a] = steps_map[y][x] + 1
                to_visit.append((a, y))


def part2(infile):
    top_map = []
    loc_S = None
    loc_E = None
    with open(infile, "r") as f:
        line = 0
        for row in f:
            top_map.append([c for c in row.strip()])
            if "S" in top_map[-1]:
                loc_S = (row.index("S"), line)
            if "E" in top_map[-1]:
                loc_E = (row.index("E"), line)
            line += 1
    e_x, e_y = loc_E
    s_x, s_y = loc_S
    top_map[e_y][e_x] = "z"
    top_map[s_y][s_x] = "a"
    height = len(top_map)
    width = len(top_map[0])
    steps_map = [[0 for _ in top_map[0]] for _ in top_map]
    steps_map[e_y][e_x] = 1
    loc = loc_E
    to_visit = []
    x, y = loc
    for i in [-1, 1]:
        a = x + i
        b = y + i
        if (
            0 <= b < height
            and steps_map[b][x] == 0
            and ord(top_map[b][x]) >= ord(top_map[y][x]) - 1
        ):
            steps_map[b][x] = steps_map[y][x] + 1
            to_visit.append((x, b))
        if (
            0 <= a < width
            and steps_map[y][a] == 0
            and ord(top_map[y][a]) >= ord(top_map[y][x]) - 1
        ):
            steps_map[y][a] = steps_map[y][x] + 1
            to_visit.append((a, y))
    # return to_visit
    while to_visit:
        x, y = to_visit.pop(0)
        if top_map[y][x] == "a":
            return steps_map[y][x] - 1
        for i in [-1, 1]:
            a = x + i
            b = y + i
            if (
                0 <= b < height
                and steps_map[b][x] == 0
                and ord(top_map[b][x]) >= ord(top_map[y][x]) - 1
            ):
                steps_map[b][x] = steps_map[y][x] + 1
                to_visit.append((x, b))
            if (
                0 <= a < width
                and steps_map[y][a] == 0
                and ord(top_map[y][a]) >= ord(top_map[y][x]) - 1
            ):
                steps_map[y][a] = steps_map[y][x] + 1
                to_visit.append((a, y))


def main():
    if args.p == 1:
        print(part1(args.f))
    if args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError("Solution for this part is not yet implemented")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
