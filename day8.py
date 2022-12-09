import argparse

def get_grid(infile):
        cols = []
        rows = []
    with open(infile, 'r') as f:
        for line in f:
            rows.append(line.strip())
        


def part1(infile):
    grid = get_grid(infile)

def main():
    if args.p == 1:
        print(part1(args.f))
    else:
        raise NotImplementedError('Solution for that part has not been implemented')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()