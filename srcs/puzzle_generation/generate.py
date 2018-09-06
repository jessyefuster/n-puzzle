#!/usr/bin/python3
import sys
import argparse
import random

def printPuzzle(puzzle, solv, size):
	print("#{}".format('solvable' if solv else 'unsolvable'))
	print(size)
	for line in puzzle:
		for cell in line:
			print(cell, end=' ')
		print()



# def orderedPuzzle(size):
# 	"""
# 	Normal goal mode
# 	"""
# 	puzzle = [ [0] * size for i in range(0, size) ]
# 	number = 1

# 	for y, line in enumerate(puzzle):
# 		for x, cell in enumerate(line):
# 			puzzle[y][x] = 0 if ( y == size - 1 and x == size - 1 ) else number

# 			number += 1

# 	return (puzzle)

def orderedPuzzle(size):
	"""
	Snail goal mode
	"""
	tsize = size * size;
	puzzle = [ [0] * size for i in range(0, size) ]
	numbers = list(range(1, tsize))
	numbers.append(0)

	x = 0
	y = 0
	ix = 1
	iy = 0
	maxx = 0
	maxy = 0

	for i in range(0, tsize):
		nx = x + ix
		ny = y + iy

		puzzle[y][x] = numbers[i]

		if nx < 0 or nx >= size or (ix != 0 and ((nx >= size + maxx) if ix > 0 else (nx < 0 - maxx))):
			if nx <= 0 or (ix < 0 and nx < 0 - maxx):
				maxx -= 1
			iy = ix
			ix = 0

		elif ny < 0 or ny >= size or (iy != 0 and ((ny >= size + maxy) if iy > 0 else (ny < 0 - maxy))):
			if ny >= size or (iy > 0 and ny >= size + maxy):
				maxy -= 1
			ix = -iy
			iy = 0

		x += ix
		y += iy

	return (puzzle)



def shufflePuzzle(puzzle, iterations):
	def findEmptyCell():
		for y, line in enumerate(puzzle):
			try:
				x = line.index(0)
				return (y, x)
			except ValueError:
				pass
	### SWAP FUNCTIONS ###
	def swapUp(y, x):
		if y == 0:
			raise KeyError
		puzzle[y][x], puzzle[y - 1][x] = puzzle[y - 1][x], puzzle[y][x]
	def swapDown(y, x):
		puzzle[y][x], puzzle[y + 1][x] = puzzle[y + 1][x], puzzle[y][x]
	def swapLeft(y, x):
		if x == 0:
			raise KeyError
		puzzle[y][x], puzzle[y][x - 1] = puzzle[y][x - 1], puzzle[y][x]
	def swapRight(y, x):
		puzzle[y][x], puzzle[y][x + 1] = puzzle[y][x + 1], puzzle[y][x]
	### MAIN SWAP ###
	def randomSwap(y, x):
		swap = {
			'u': swapUp,
			'd': swapDown,
			'l': swapLeft,
			'r': swapRight
		}
		move = random.choice(['u', 'd', 'l', 'r'])

		try:
			swap[move](emptyCellY, emptyCellX)
		except Exception as e:
			randomSwap(y, x)


	for i in range(0, iterations):
		emptyCellY, emptyCellX = findEmptyCell()
		randomSwap(emptyCellY, emptyCellX)

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


	printPuzzle(puzzle, solvable, args.size)
