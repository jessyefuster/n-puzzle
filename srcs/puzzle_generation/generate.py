#!/usr/bin/python3
import sys
import argparse
import random

def printPuzzle(puzzle, solv):
	print("#{}".format('solvable' if solv else 'unsolvable'))
	for line in puzzle:
		for box in line:
			print(box, end=' ')
		print()



def orderedPuzzle(size):
	puzzle = [ [0] * size for i in range(0, size) ]
	number = 1

	for y, line in enumerate(puzzle):
		for x, box in enumerate(line):
			puzzle[y][x] = 0 if ( y == size - 1 and x == size - 1 ) else number

			number += 1

	return (puzzle)



def shufflePuzzle(puzzle, iterations):
	return (puzzle)



def generatePuzzle(size, solvable, iterations):

	puzzle = orderedPuzzle(size)
	puzzle = shufflePuzzle(puzzle, iterations)

	# MAKE UNSOLVABLE
	if not solvable:
		if puzzle[0][0] == 0 or puzzle[0][1] == 0:
			puzzle[size - 1][-1], puzzle[size - 1][-2] = puzzle[size - 1][-2], puzzle[size - 1][-1]
		else:
			puzzle[0][0], puzzle[0][1] = puzzle[0][1], puzzle[0][0]

	return(puzzle)



if __name__ == '__main__':


	# ARGUMENT PARSING
	parser = argparse.ArgumentParser(description="N-puzzle generator")

	parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >2.")
	parser.add_argument("-s", "--solvable", action="store_true", default=False, help="forces generation of a solvable puzzle")
	parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="forces generation of an unsolvable puzzle")
	parser.add_argument("-i", "--iterations", type=int, default=1000, help="number of swaps for shuffling", metavar="")

	args = parser.parse_args()


	# CHECKING VALIDITY
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


	# PUZZLE MAKING
	puzzle = generatePuzzle(size=args.size, solvable=solvable, iterations=args.iterations)


	printPuzzle(puzzle, solvable)
