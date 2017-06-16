#!/usr/bin/python3
import sys

def solvable(puzzle):
	iterations = 0
	flatPuzzle = []

	# FLATTEN PUZZLE
	for line in puzzle:
		flatPuzzle += line
	flatPuzzle.remove(0)

	for i, value in enumerate(flatPuzzle):
		print(flatPuzzle[i + 1:])
		for nextValue in flatPuzzle[i + 1:]:
			if nextValue < value:
				iterations += 1

	if iterations % 2 == 0: #even
		return (True)
	else: #odd
		return (False)

if __name__ == '__main__':

	# solvable
	# puzzle = [	[5, 12, 7, 13],
	# 			[15, 8, 0, 6],
	# 			[14, 4, 3, 2],
	# 			[9, 1, 11, 10]	]

	# unsolvable
	puzzle = [	[1, 2, 3],
				[4, 5, 8],
				[7, 0, 6]	]

	if not solvable(puzzle):
		print("Not solvable")
	else:
		print("Solvable")