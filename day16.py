import re
import itertools
from argparse import ArgumentParser


def read_puzzle(file):
    with open(file, "r") as f:
        return [re.findall("[A-Z]+|\d+", line[1:]) for line in f.readlines()]
        # List of lists: [valvename, flow, *neighbors]


def solve(puzzle):
    graph = {valve: leads for valve, _, *leads in puzzle}
    # dictionary of neighbors
    flows = {valve: int(flow) for valve, flow, *_ in puzzle if flow != "0"}
    # dictionary of nonzero flows
    indices = {valve: 1 << i for i, valve in enumerate(flows)}
    # 1-bit mask for valves
    distances = {(v, l): 1 if l in graph[v] else 1000 for l in graph for v in graph}
    for k, i, j in itertools.permutations(graph, 3):
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    def visit(valve, minutes, bitmask, pressure, answer):
        answer[bitmask] = max(answer.get(bitmask, 0), pressure)
        for valve2, flow in flows.items():
            remaining_minutes = minutes - distances[valve, valve2] - 1
            if indices[valve2] & bitmask or remaining_minutes <= 0:
                continue
            visit(
                valve2,
                remaining_minutes,
                bitmask | indices[valve2],
                pressure + flow * remaining_minutes,
                answer,
            )
        return answer

    part1 = max(visit("AA", 30, 0, 0, {}).values())
    visited2 = visit("AA", 26, 0, 0, {})
    part2 = max(
        v1 + v2
        for bitm1, v1 in visited2.items()
        for bitm2, v2 in visited2.items()
        if not bitm1 & bitm2
    )
    return part1, part2


def main():
    puzzle = read_puzzle(args.f)
    if args.p == 1:
        print(solve(puzzle)[0])
    elif args.p == 2:
        print(solve(puzzle)[1])
    else:
        raise NotImplementedError("No solution implemented for that part")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("f", type=str)
    args = parser.parse_args()
    main()
