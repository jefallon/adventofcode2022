import argparse

class ElfFolder:
    def __init__(self, parent=None,sizelist = None, name = None):
        self.filesize = 0
        self.size = 0
        self.parent = parent
        self.sub = {}
        self.contrib = 0
        self.sizelist = sizelist
        if self.parent:
            self.name = self.parent.name+'/'+name
        else:
            self.name = ''

    def folder_size(self):
        contrib = 0
        for k,f in self.sub.items():
            f.folder_size()
            self.size += f.size
            contrib += f.contrib
        self.size += self.filesize
        if self.size <= 100000:
            contrib += self.size
        self.contrib = contrib
        self.sizelist[self.name] = self.size

def get_filesystem(infile):
    sizes = {}
    root = ElfFolder(sizelist=sizes)
    current_dir = root
    current_dir.sub['/'] = ElfFolder(current_dir,sizes,'')
    with open(infile,'r') as f:
        for row in f:
            std = row.strip().split()
            if std[0] == '$':
                if std[1] == 'cd':
                    if std[2] == '..':
                        current_dir = current_dir.parent
                        continue
                    current_dir = current_dir.sub[std[2]]
                    continue
            if std[0].isnumeric():
                current_dir.filesize += int(std[0])
                continue
            if std[0] == 'dir':
                current_dir.sub[std[1]] = ElfFolder(current_dir,sizes,std[1])
    root.folder_size()
    return root, sizes

def part1(infile):
    root = get_filesystem(infile)[0]
    return root.contrib

def part2(infile):
    root, sizes = get_filesystem(infile)
    space_needed = 30000000
    space_available = 70000000-root.size
    space_to_make = space_needed - space_available
    least_delete = min(y for y in sizes.values() if y > space_to_make)
    return least_delete


def main():
    if args.p == 1:
        print(part1(args.f))
    elif args.p == 2:
        print(part2(args.f))
    else:
        raise NotImplementedError('No solution has been implemented for this part')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('f', type=str)
    args = parser.parse_args()
    main()