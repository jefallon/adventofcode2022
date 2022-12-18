from functools import reduce
from argparse import ArgumentParser
from re import findall

def part1(infile):
    beacons = set()
    not_beacons = {}
    with open(infile, 'r') as f:
        for row in f:
            sx, bx = list(map(int,findall('x=(-?\d+)', row)))
            sy, by = list(map(int,findall('y=(-?\d+)', row)))
            beacons.add((bx,by))
            man_dist = abs(sx-bx)+abs(sy-by)
            for y_val in range(-man_dist,man_dist+1):
                x_rad = abs(man_dist-abs(y_val))
                if sy+y_val not in not_beacons:
                    not_beacons[sy+y_val] = [[sx-x_rad,sx+x_rad]]
                    continue
                for r in not_beacons[sy+y_val]:
                    if r[0]<=(sx-x_rad)<=r[1]:
                        if (sx + x_rad) > r[1]:
                            r[1] = sx + x_rad
                            break
                    if r[0] <= (sx+x_rad) <= r[1]:
                        if (sx- x_rad)< r[0]:
                            r[0] = sx - x_rad
                            break
                else:
                    not_beacons[sy+y_val].append([sx-x_rad, sx+x_rad])
    not_beacons = [set(range(x,y+1)) for x,y in not_beacons[2000000]]
    not_beacons= reduce(lambda x,y:x.union(y), not_beacons)
    beacons = len([b for b in beacons if b[1]==2000000])
    return len(not_beacons)-beacons


def main():
    if args.p==1:
        print(part1(args.f))
    else:
        raise NotImplementedError('Solution for this part not yet implemented')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()