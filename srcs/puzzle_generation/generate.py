#!/usr/bin/python3
import sys
import argparse
import random

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="N-puzzle generator")

	parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >2.")
	parser.add_argument("-s", "--solvable", action="store_true", default=False, help="forces generation of a solvable puzzle")
	parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="forces generation of an unsolvable puzzle")

	args = parser.parse_args()


	if args.size < 3:
		print("Puzzle's size must at least 3.")
		sys.exit(1)

	if args.solvable and args.unsolvable:
		print("Puzzle can't be solvable and unsolvable at the same time.")
		sys.exit(1)

	if not args.solvable and not args.unsolvable:
		solvable = random.choice([True, False])
	else:
		solvable = True if args.solvable else False
