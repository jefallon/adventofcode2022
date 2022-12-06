import argparse

def part1(infile):
    with open(infile, 'r') as f:
        row = next(f)
        num_piles = len(row)//4
        piles = [[] for _ in range(num_piles+1)]
        while row[1] != '1':
            for i in range(num_piles):
                crate = row[4*i+1]
                if crate != ' ':
                    piles[i+1].append(crate)
            row = next(f)
        piles = [x[::-1] for x in piles]
        row = next(f)
        for row in f:
            crates, source, dest = map(int,row.strip().split()[1::2])
            while crates:
                crates -= 1
                piles[dest].append(piles[source].pop())
    msg = ''.join(p[-1] for p in piles[1:] if p[0])
    return msg

def part2(infile):
    with open(infile, 'r') as f:
        row = next(f)
        num_piles = len(row)//4
        piles = [[] for _ in range(num_piles+1)]
        while row[1] != '1':
            for i in range(num_piles):
                crate = row[4*i+1]
                if crate != ' ':
                    piles[i+1].append(crate)
            row = next(f)
        piles = [x[::-1] for x in piles]
        row = next(f)
        for row in f:
            crates, source, dest = map(int,row.strip().split()[1::2])
            piles[dest].extend(piles[source][-crates:])
            piles[source] = piles[source][:-crates]
    msg = ''.join(p[-1] for p in piles[1:] if p[0])
    return msg


def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('Solution for that part is not yet implemented')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()