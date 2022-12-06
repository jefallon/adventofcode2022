import argparse

def part1(infile):
    with open(infile, 'r') as f:
        row = next(f)
        num_piles = len(row)//3 + 1
        piles = [[]]*(num_piles+1)
        while row[1] != '1':
            print(len(row), num_piles)
            for i in range(num_piles-1):
                crate = row[3*i+1]
                if crate:
                    piles[i+1].append(crate)
            row = next(f)
    return piles

def main():
    if args.p == 1:
        print(part1(args.f))
    else:
        raise NotImplementedError('Solution for that part is not yet implemented')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()