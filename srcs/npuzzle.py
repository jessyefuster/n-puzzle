#!/usr/bin/python3
import sys
import copy
import random
import heapq
import argparse

from ntree import *
from puzzle_generation import generate

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

	def findEmptyCell(self, puzzle):
		for y, line in enumerate(puzzle):
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
		flatPuzzle = self.flatten(self.puzzle)
		flatPuzzle.remove(0)

		for i, value in enumerate(flatPuzzle):
			for nextValue in flatPuzzle[i + 1:]:
				if nextValue < value:
					iterations += 1
		if self.size % 2 == 1 and iterations % 2 == 0:
			return (True)
		if self.size % 2 == 0:
			blankRowTop = (self.findEmptyCell(self.puzzle)[0] + 1)
			blankRow = self.size - blankRowTop + 1
			if blankRow % 2 == 0 and iterations % 2 == 1:
				return (True)
			if blankRow % 2 == 1 and iterations % 2 == 0:
				return (True)
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
					dist += abs(start_x - end_x) + abs(start_y - end_y)
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
					dist += ( (start_x - end_x) ** 2 + (start_y - end_y) ** 2 ) ** 0.5
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
	def nextStates(self, baseState):
		empty = self.findEmptyCell(baseState.puzzle)
		nextStates = []
		
		for swap in self.swaps:
			puzzle = copy.deepcopy(baseState.puzzle)
			puzzle = swap(puzzle, empty)
			
			if puzzle:
				nextStates.append(StateNode(puzzle=puzzle, g=baseState.g, h=self.heuristic(puzzle), parent=baseState))

		return (nextStates)


	def better(self, OpenSet, State):
		for t in OpenSet:
			if t[1].puzzle == State.puzzle and t[1].cost <= State.cost:
				return (True)
		return (False)


	def aStar(self):
		OpenSet = []
		closedSet = {}

		firstNode = StateNode(puzzle=self.puzzle, g=0, h=self.heuristic(self.puzzle), parent=None)
		heapq.heappush(OpenSet, (firstNode.cost, firstNode))

		while OpenSet:
			leastCostState = heapq.heappop(OpenSet)[1]
			nextStates = self.nextStates(leastCostState)

			for state in nextStates:
				if self.resolved(state.puzzle):
					print("Solution found")
					return (state)
				if self.better(OpenSet, state) or (state.key in closedSet and closedSet[state.key].cost <= state.cost):
					pass
				else:
					heapq.heappush(OpenSet, (state.cost, state))

			closedSet[leastCostState.key] = leastCostState
	#################

	def costs(self):
		print(self.manhattan(self.puzzle))
		print(self.euclidian(self.puzzle))
		print(self.misplaced(self.puzzle))


	###   SOLVE   ###
	def resolved(self, puzzle):
		return (puzzle == self.goal)


	def resolve(self):
		result = self.aStar()

		print(self.printPuzzle(result.puzzle))
		while result.parent != None:
			result = result.parent
			# print(self.printPuzzle(result.puzzle))
	#################
		





if __name__ == '__main__':
	test = generate.generatePuzzle(5, True, 200)

	P = Puzzle(test)
	P.printPuzzle(test)

	if not P.solvable():
		print("Not solvable")
	else:
		P.resolve()
