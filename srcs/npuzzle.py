#!/usr/bin/python3
import sys
import copy

class Puzzle:
	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.size = len(puzzle)
		self.tsize = pow(self.size, 2)

		self.goal = self.makeGoal()

		self.heuristic = self.manhattan
		self.swaps = [self.swapUp, self.swapDown, self.swapLeft, self.swapRight]


	###   TOOLS   ###
	def printPuzzle(self, puzzle):
		for line in puzzle:
			for cell in line:
				print(cell, end=' ')
			print()

	def makeGoal(self):
		puzzle = [ [0] * self.size for i in range(0, self.size) ]
		number = 1

		for y, line in enumerate(puzzle):
			for x, cell in enumerate(line):
				puzzle[y][x] = 0 if ( y == self.size - 1 and x == self.size - 1 ) else number

				number += 1

		return (puzzle)

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

	def searchPosition(self, value):
		for y, line in enumerate(self.goal):
			for x, number in enumerate(line):
				if value == number:
					return (x, y)
	#################


	### HEURISTIC ###
	def	manhattan(self, puzzle):
		'''
		dist = (start_x - end_x) + (start_y - end_y)
		'''
		dist = 0

		for start_y, line in enumerate(puzzle):
			for start_x, value in enumerate(line):
				if value:
					end_x, end_y = self.searchPosition(value)
					dist += abs(start_x - start_y) + abs(end_x - end_y)
		return (dist)

	def	euclidian(self, puzzle):
		'''
		dist = sqrt( (ax - bx)**2 + (ay - by)**2 )
		'''
		dist = 0

		for start_y, line in enumerate(puzzle):
			for start_x, value in enumerate(line):
				if value:
					end_x, end_y = self.searchPosition(value)
					dist += ( (start_x - start_y) ** 2 + (start_x - start_y) ** 2 ) ** 0.5
		return (dist)

	def	misplaced(self, puzzle):
		dist = 0

		for y, line in enumerate(puzzle):
			for x, value in enumerate(line):
				if value:
					if (x, y) != self.searchPosition(value):
						dist += 1
		return (dist)
	#################

	###   SWAPS   ###
	def swapUp(self, puzzle, empty):
		y, x = empty
		if y - 1 >= 0:
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
		if x - 1 >= 0:
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
				nextStates.append(puzzle)

		return (nextStates)

	def nextStep(self):
		nextArray = self.nextStates()
		costArray = []
		for state in nextArray:
			costArray.append(self.heuristic(state))

		# self.printPuzzle(self.puzzle)
		# print(costArray)
		# print()
		# for state in nextArray:
		# 	self.printPuzzle(state)
		# 	print()

		# print("\n==============")
		# print()

		leastCost = min(costArray)
		if costArray.count(leastCost) > 1:
			pass

		optimalState = nextArray[costArray.index(min(costArray))]

		return (optimalState)
	#################


	###   SOLVE   ###
	def resolved(self):
		flat = self.flatten(self.puzzle)
		return (flat == self.goal)


	def resolve(self):
		i = 0

		while not self.resolved() and i < 5:
			self.puzzle = self.nextStep()
			# self.printPuzzle(self.puzzle)
			# print()
			i += 1
	#################
		





if __name__ == '__main__':

	# solvable
	puzzle = [	[5, 12, 7, 13],
				[15, 8, 0, 6],
				[14, 4, 3, 2],
				[9, 1, 11, 10]	]


	P = Puzzle(puzzle)



	if not P.solvable():
		print("Not solvable")
	else:
		P.resolve()
