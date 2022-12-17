from argparse import ArgumentParser

def get_rocks(infile):
    blocked = {}
    with open(infile, 'r') as f:
        for row in f:
            path  = row.strip().split()[::2]
            rock = list(map(int,path[0].split(',')))
            for point in path[1:]:
                point = list(map(int,point.split(',')))
                if rock[0] == point[0]:
                    if not rock[0] in blocked:
                        blocked[rock[0]] = set()
                    y1,y2 = min(point[1],rock[1]), max(point[1],rock[1])
                    blocked[rock[0]].update(set(range(y1,y2+ 1)))
                else:
                    x1,x2 = min(rock[0], point[0]), max(rock[0], point[0])
                    for x in range(x1, x2+1):
                        if not x in blocked:
                            blocked[x] = set()
                        blocked[x].add(rock[1])
                rock = point
    return blocked

def part1(infile):
    blocked = get_rocks(infile)
    sand = -1
    while True:
        sand += 1
        pos = [500,min(blocked[500]) - 1]
        while True:
            while pos[1]+1 not in blocked[pos[0]]:
                pos[1] += 1
            if pos[0] - 1 not in blocked:
                return sand
            if pos[1] + 1 in blocked[pos[0]-1]:
                if pos[0] + 1 not in blocked:
                    return sand
                if pos[1]+1 in blocked[pos[0]+1]:
                    blocked[pos[0]].add(pos[1])
                    break
                pos[0] += 1
                pos[1] += 1
                continue
            pos[0] -= 1
            pos[1] += 1
            if pos[1] > max(blocked[pos[0]]):
                return sand

def part2(infile):
    blocked = get_rocks(infile)
    floor = 2+max(max(y) for y in blocked.values())
    # return floor
    for x in blocked:
        blocked[x].add(floor)
    sand = 0
    pos = [500,min(blocked[500])-1]
    while 0 not in blocked[500]:
        while pos[1]+1 not in blocked[pos[0]]:
            pos[1] += 1
        if pos[0] - 1 not in blocked:
            blocked[pos[0]-1] = {floor-1,floor}
            pos = [500,min(blocked[500])-1]
            sand += 1
            continue
        if pos[1]+1 in blocked[pos[0]-1]:
            if pos[0] + 1 not in blocked:
                blocked[pos[0]+1] = {floor-1,floor}
                pos = [500,min(blocked[500])-1]
                sand += 1
                continue
            if pos[1]+1 in blocked[pos[0]+1]:
                blocked[pos[0]].add(pos[1])
                pos = [500,min(blocked[500])-1]
                sand += 1
                continue
            pos[0] += 1
            pos[1] += 1
            continue
        pos[0] -=1
        pos[1] += 1
    return sand

def main():
    if args.p == 1:
        print(part1(args.f))
    if args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('Solution for that part is not yet implemented')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()