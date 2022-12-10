import argparse

def part1(infile):
    cycle = 0
    register = 1
    signal_strength = 0
    with open(infile, 'r') as f:
        for row in f:
            cycle += 1
            line = row.strip().split()
            # print(cycle, register)
            signal_strength += check_cycle(cycle,register)
            if line[0] == 'noop':
                continue
            cycle += 1
            # print(cycle, register)
            signal_strength += check_cycle(cycle, register)
            register += int(line[1])
    return signal_strength

def part2(infile):
    sprite = 1
    cycle = 0
    image = []
    with open(infile, 'r') as f:
        for row in f:
            line = row.strip().split()
            if not cycle:
                image.append([])
            print(cycle, sprite)
            if cycle in range(sprite-1,sprite+2):
                image[-1].append('#')
            else:
                image[-1].append('.')
            cycle += 1
            cycle %= 40
            if line[0] == 'noop':
                continue
            if not cycle:
                image.append([])
            print(cycle, sprite)
            if cycle in range(sprite-1, sprite+2):
                image[-1].append('#')
            else:
                image[-1].append('.')
            sprite += int(line[1])
            cycle += 1
            cycle %= 40
    for x in image:
        print(''.join(x))

def check_cycle(cycle, register):
    if not (cycle-20)%40:
        return cycle*register
    return 0

def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        part2(args.f)
    else:
        raise NotImplementedError('Solution for this part is not yet implemented')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()