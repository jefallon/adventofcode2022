import argparse

def prio(l):
	n = ord(l)
	p = (n>95)*(n-96) + (n<95)*(n-38)
	return p

def part1(infile):
	wrong = 0
	with open(infile, 'r') as f:
		for row in f:
			sack = row.strip()
			s = len(sack)
			c = s//2
			miss = set(sack[:c]).intersection(set(sack[c:])).pop()
			wrong += prio(miss)
	return wrong

def part2(infile):
	badges = 0
	with open(infile, 'r') as f:
		for row in f:
			badges += prio(set(row.strip()).intersection(set(next(f).strip())).intersection(set(next(f).strip())).pop())
	return badges

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