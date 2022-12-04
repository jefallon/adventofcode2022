import argparse

def part1(infile):
	overlaps = 0
	with open(infile, 'r') as f:
		for row in f:
			elf1,elf2 = row.strip().split(',')
			a,b = list(map(int,elf1.split('-')))
			x,y = list(map(int,elf2.split('-')))
			if a <= x and b >= y:
				overlaps += 1
				continue
			if x <= a and y >= b:
				overlaps += 1
	return overlaps

def part2(infile):
	overlaps = 0
	with open(infile, 'r') as f:
		for row in f:
			elf1, elf2 = row.strip().split(',')
			a,b = list(map(int,elf1.split('-')))
			x,y = list(map(int,elf2.split('-')))
			if b < x or y < a:
				continue
			overlaps += 1
	return overlaps


def main():
	if args.p == 1:
		print(part1(args.f))
	elif args.p == 2:
		print(part2(args.f))
	else:
		raise NotImplementedError('Solution for this part not yet implemented')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('p', type=int)
	parser.add_argument('f', type=str)
	args = parser.parse_args()
	main()