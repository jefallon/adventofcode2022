import argparse

class Obsidian():
    def __init__(self):
        self.cubes = {}

    def add_cube(self, x,y,z):
        if x not in self.cubes:
            self.cubes[x] = {y:{z:6}}
        elif y not in self.cubes[x]:
            self.cubes[x][y] = {z:6}
        elif z not in self.cubes[x][y]:
            self.cubes[x][y][z] = 6
        self.fix_sides(x,y,z)
        return

    def fix_sides(self, x,y,z):
        adj = [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]
        for block in adj:
            a,b,c = block
            if a in self.cubes and b in self.cubes[a] and c in self.cubes[a][b] and (a,b,c) != (x,y,z):
                self.cubes[a][b][c] -=1
                self.cubes[x][y][z] -=1


def main():
    obs = Obsidian()
    with open(args.f, 'r') as f:
        for row in f:
            x,y,z = map(int,row.strip().split(','))
            obs.add_cube(x,y,z)
    if args.p == 1:
        print(sum(sum(sum(z.values()) for z in y.values()) for y in obs.cubes.values()))
    else:
        raise NotImplementedError('Solution for that part not implemented or invalid part input')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('f', type = str)
    parser.add_argument('p', type = int)
    args = parser.parse_args()
    main()