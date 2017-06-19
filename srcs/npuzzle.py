#!/usr/bin/python3
import sys
import copy

class Puzzle:
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.size = len(puzzle)
		self.tsize = pow(self.size, 2)

		self.goal = list(range(1, self.tsize))
		self.goal.append(0)

		self.swaps = [self.swapUp, self.swapDown, self.swapLeft, self.swapRight]


	###   TOOLS   ###
	def printPuzzle(self, puzzle):
		for line in puzzle:
			for cell in line:
				print(cell, end=' ')
			print()

	def findEmptyCell(self):
		for y, line in enumerate(self.puzzle):
			try:
				x = line.index(0)
				return (y, x)
			except ValueError:
				pass

	def flatten(self, puzzle):
		flatPuzzle = []

		for line in puzzle:
			flatPuzzle += line

		return (flatPuzzle)

	def solvable(self):
		iterations = 0
		flatPuzzle = self.flatten(puzzle)
		flatPuzzle.remove(0)

		for i, value in enumerate(flatPuzzle):
			for nextValue in flatPuzzle[i + 1:]:
				if nextValue < value:
					iterations += 1

		if iterations % 2 == 0: #even
			return (True)
		else: #odd
			return (False)
	#################


	###   SWAPS   ###
	def swapUp(self, puzzle, empty):
		y, x = empty
		if y - 1 > 0:
			puzzle[y][x], puzzle[y - 1][x] = puzzle[y - 1][x], puzzle[y][x]
			return (puzzle)
		return (False)
	def swapDown(self, puzzle, empty):
		y, x = empty
		if y + 1 < self.size:
			puzzle[y][x], puzzle[y + 1][x] = puzzle[y + 1][x], puzzle[y][x]
			return (puzzle)
		return (False)
	def swapLeft(self, puzzle, empty):
		y, x = empty
		if x - 1 > 0:
			puzzle[y][x], puzzle[y][x - 1] = puzzle[y][x - 1], puzzle[y][x]
			return (puzzle)
		return (False)
	def swapRight(self, puzzle, empty):
		y, x = empty
		if x + 1 < self.size:
			puzzle[y][x], puzzle[y][x + 1] = puzzle[y][x + 1], puzzle[y][x]
			return (puzzle)
		return (False)
	#################


	###   MOVES   ###
	def nextStates(self):
		empty = self.findEmptyCell()
		nextStates = []
		
		for swap in self.swaps:
			puzzle = copy.deepcopy(self.puzzle)
			puzzle = swap(puzzle, empty)
			
			if puzzle:
				self.printPuzzle(puzzle)
				print()
				nextStates.append(puzzle)

	def nextStep(self):
		nextArray = self.nextStates()
	#################


	###   SOLVE   ###
	def resolved(self):
		flat = self.flatten(self.puzzle)
		return (flat == self.goal)


	def resolve(self):
		if not self.resolved():
			self.puzzle = self.nextStep()
	#################
		





if __name__ == '__main__':

	# solvable
	puzzle = [	[5, 12, 0, 13],
				[15, 8, 7, 6],
				[14, 4, 3, 2],
				[9, 1, 11, 10]	]


	P = Puzzle(puzzle)
	P.printPuzzle(P.puzzle)
	print('\n=============')

	# if not P.solvable():
	# 	print("Not solvable")
	# else:
	P.resolve()
