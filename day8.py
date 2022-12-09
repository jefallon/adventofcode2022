import argparse

def get_grid(infile):
    cols = []
    rows = []
    with open(infile, 'r') as f:
        for line in f:
            rows.append(line.strip())
    cols = [''.join(s[i] for s in rows) for i in range(len(rows))]
    return rows, cols
        


def part1(infile):
    rows, cols = get_grid(infile)
    nrows = len(rows)
    ncols = len(cols)
    visible = 2*nrows+2*ncols - 4
    for r in range(1,nrows-1):
        for c, s in enumerate(rows[r][1:-1],1):
            if all(x < s for x in rows[r][:c]) or all(x < s for x in rows[r][c+1:]):
                visible += 1
                continue
            if all(x < s for x in cols[c][:r]) or all (x < s for x in cols[c][r+1:]):
                visible += 1
                continue
    return visible

def part2(infile):
    rows, cols = get_grid(infile)
    nrows = len(rows)
    ncols = len(cols)
    scenic = 0
    for r in range(1,nrows - 1):
        for c,s in enumerate(rows[r][1:-1],1):
            east = 0
            west = 0
            south = 0
            north = 0
            te = c+1
            tw = c-1
            ts = r+1
            tn = r-1
            while te < ncols:
                east += 1
                if rows[r][te] < s:
                    te += 1
                else:
                    break
            if east:
                while tw > -1:
                    west += 1
                    if rows[r][tw] < s:
                        tw -= 1
                    else:
                        break
                if west:
                    while ts < nrows:
                        south += 1
                        if rows[ts][c] < s:
                            ts += 1
                        else:
                            break
                    if south:
                        while tn > -1:
                            north += 1
                            if rows[tn][c] < s:
                                tn -=1
                            else:
                                break
            view = east*west*north*south
            scenic = max(view,scenic)
    return scenic

def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('Solution for that part has not been implemented')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()