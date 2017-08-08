class StateNode:
	"""
	This object represents a state of the N-puzzle
	"""
	def __init__(self, puzzle = None, g = 0, h = 0, parent = None):
		self.l = None
		self.r = None

		self.cost = g + h
		self.g = g
		self.h = h
		self.puzzle = puzzle
		self.parent = parent
		self.key = self.flatten()

	def __repr__(self):
		return ("<{className}(cost={self.cost}, puzzle={self.puzzle})>".format(className=self.__class__.__name__, self=self))

	def __gt__(self, other):
		return (True)

	def flatten(self):
		key = ''

		for line in self.puzzle:
			for cell in line:
				key += str(cell)

		return (key)
		


class Tree:
	"""
	This object is a binary tree that allows to sort state objects by cost
	"""
	def	__init__(self):
		self.root = None

	def getRoot(self):
		return (self.root)

	def add(self, node):
		if (self.root == None):
			self.root = node
		else:
			self._add(node, self.root)

	def _add(self, new, node):
		if (new.cost < new.cost):
			if (node.l != None):
				self._add(new, node.l)
			else:
				node.l = new
		else:
			if (node.r != None):
				self._add(new, node.r)
			else:
				node.r = new

	def find(self, val):
		if (self.root != None):
			return self._find(val, self.root)
		else:
			return (None)

	def _find(self, val, node):
		if (val == node.cost):
			return node
		elif (val < node.cost and node.l != None):
			self._find(val, node.l)
		elif (val > node.cost and node.r != None):
			self._find(val, node.r)

	def deleteTree(self):
		# garbage collector will do this for us. 
		self.root = None

	def printTree(self):
		if (self.root != None):
			self._printTree(self.root)

	def _printTree(self, node):
		if (node != None):
			self._printTree(node.l)
			print (str(node.cost) + ' ')
			self._printTree(node.r)