import argparse

def part1(infile):
    with open(infile, 'r') as f:
        for row in f:
            return find_four(row.strip())

def part2(infile):
    with open(infile, 'r') as f:
        for row in f:
            return find_fourteen(row.strip())

def find_four(string):
    for i in range(len(string) - 4):
        if len(set(string[i:i+4])) == 4:
            return i+4

def find_fourteen(string):
    for i in range(len(string) - 14):
        if len(set(string[i:i+14])) == 14:
            return i+14

def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('Solution not yet implemented for this part')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()