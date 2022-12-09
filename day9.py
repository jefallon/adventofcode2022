import argparse

class RopeKnot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited = {(0,0)}

    def move(self, direction):
        if direction == 'D':
            self.y -= 1
        elif direction == 'U':
            self.y+= 1
        elif direction == "L":
            self.x += 1
        elif direction == "R":
            self.x -= 1

    def follow(self, head):
        if head.x == self.x:
            if head.y == self.y+2:
                self.y += 1
            elif head.y == self.y-2:
                self.y -= 1
        elif head.x == self.x + 1:
            if head.y > self.y + 1:
                self.x += 1
                self.y += 1
            elif head.y < self.y - 1:
                self.x += 1
                self.y -= 1
        elif head.x == self.x - 1:
            if head.y > self.y + 1:
                self.x -= 1
                self.y += 1
            elif head.y < self.y - 1:
                self.x -= 1
                self.y -= 1
        elif head.y == self.y:
            if head.x == self.x + 2:
                self.x += 1
            elif head.x == self.x - 2:
                self.x-= 1
        elif head.y > self.y:
            if head.x > self.x:
                self.y += 1
                self.x += 1
            elif head.x < self.x:
                self.y += 1
                self.x -= 1
        else:
            if head.x > self.x:
                self.x += 1
                self.y -= 1
            elif head.x < self.x:
                self.x -= 1
                self.y -= 1

def part1(infile):
    ropehead =RopeKnot()
    ropetail = RopeKnot()
    with open(infile, 'r') as f:
        for row in f:
            direction, stepsize = row.strip().split()
            stepsize = int(stepsize)
            while stepsize:
                stepsize -= 1
                ropehead.move(direction)
                ropetail.follow(ropehead)
                ropetail.visited.add((ropetail.x, ropetail.y))
    return len(ropetail.visited)

def part2(infile):
    knots = [RopeKnot() for _ in range(10)]
    with open(infile, 'r') as f:
        for row in f:
            direction,stepsize = row.strip().split()
            stepsize = int(stepsize)
            while stepsize:
                stepsize -= 1
                knots[0].move(direction)
                for i in range(1,10):
                    knots[i].follow(knots[i-1])
                knots[-1].visited.add((knots[-1].x,knots[-1].y))
    return len(knots[-1].visited)

def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p== 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('Solution for that part is not yet implemented')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()