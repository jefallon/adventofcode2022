import argparse
from math import lcm

class Monkey:
    def __init__(self):
        self.items = []
        self.op = ""
        self.mod = 0
        self.test_t = None
        self.test_f = None
        self.inspections = 0
        self.tosses = {}

    def check_worry(self, item):
        old = item
        new = eval(self.op)
        new //= 3
        if new%self.mod:
            self.tosses[self.test_f].append(new)
        else:
            self.tosses[self.test_t].append(new)
        self.inspections += 1


    def check_worry_2(self,item, e_mod):
        old = item
        new = eval(self.op)
        new %= e_mod
        if new%self.mod:
            self.tosses[self.test_f].append(new)
        else:
            self.tosses[self.test_t].append(new)
        self.inspections += 1

def part1(infile):
    monkeys = get_monkeys(infile)
    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.check_worry(item)
            monkey.items = []
            for idx, items in monkey.tosses.items():
                monkeys[idx].items.extend(items)
            monkey.tosses = {monkey.test_f:[], monkey.test_t:[]}
    monkeys.sort(key = lambda x:x.inspections)
    return monkeys[-2].inspections*monkeys[-1].inspections

def part2(infile):
    monkeys = get_monkeys(infile)
    e_mod = lcm(*(m.mod for m in monkeys))
    for round in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.check_worry_2(item, e_mod)
            monkey.items = []
            for idx, items in monkey.tosses.items():
                monkeys[idx].items.extend(items)
            monkey.tosses = {monkey.test_f:[], monkey.test_t:[]}
    # return [m.inspections for m in monkeys]
    monkeys.sort(key = lambda x:x.inspections)
    return monkeys[-2].inspections*monkeys[-1].inspections

def get_monkeys(infile):
    monkeys = []
    with open(infile, 'r') as f:
        for row in f:
            line = row.strip().replace(',','').split()
            if not line:
                continue
            if line[0] == 'Monkey':
                monkeys.append(Monkey())
                continue
            monkey = monkeys[-1]
            if line[0] == 'Starting':
                for item in line[2:]:
                    monkey.items.append(int(item))
                continue
            if line[0] == "Operation:":
                monkey.op = ' '.join(line[3:])
                continue
            if line[0] == "Test:":
                monkey.mod = int(line[-1])
                continue
            if line[1] == "true:":
                monkey.test_t = int(line[-1])
                continue
            if line[1] == "false:":
                monkey.test_f = int(line[-1])
                monkey.tosses = {monkey.test_f:[], monkey.test_t:[]}
                continue
    return monkeys

def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('Solution for that part not implemented')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()