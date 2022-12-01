import argparse

def part_a(infile):
    with open(infile, 'r') as f:
        cal_elf = 0
        this_elf = 0
        for row in f:
            line = row.strip()
            if line == '':
                cal_elf = max(cal_elf, this_elf)
                this_elf = 0
                continue
            this_elf += int(line)
        cal_elf = max(cal_elf, this_elf)
    return cal_elf

def part_b(infile):
    with open(infile, 'r') as f:
        top_elves = [0,0,0]
        this_elf = 0
        for row in f:
            line = row.strip()
            if line == '':
                for elf in range(3):
                    if this_elf > top_elves[elf]:
                        top_elves = top_elves[:elf] + [this_elf] + top_elves[elf:2]
                        break
                this_elf = 0
                continue
            this_elf += int(line)
        for elf in range(3):
            if this_elf > top_elves[elf]:
                top_elves = top_elves[:elf] + [this_elf] + top_elves[elf:2]
                break
    top_three = sum(top_elves)
    return top_three

def main():
    if args.p == 1:
        print(part_a(args.f))
    elif args.p == 2:
        print(part_b(args.f))
    else:
        raise NotImplementedError("There is no solution for this part, or the part does not exist")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()
