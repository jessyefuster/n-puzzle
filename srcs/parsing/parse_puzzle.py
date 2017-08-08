import re
import sys

var_length = []

def cast_to_int(puzzle):
	for y, line in enumerate(puzzle):
		for x, index in enumerate(line):
			puzzle[y][x] = int(puzzle[y][x])

def check_all_number(puzzle):
	tab = []
	for line in puzzle:
		for value in line:
			tab.append(value)

	tab = [item for sublist in puzzle for item in sublist]
	tab = [int(i) for i in tab]

	tab = sorted(tab)

	for i in range(max(tab)):
		if ((i + 1) != tab[i + 1]):
			print('error: Invalid value')
			return (False)
	return (True)


def check_if_good(puzzle):
	check_len_line = []
	for tab in puzzle:
		i = 0
		check_len_line.append(len(tab))
		for value in tab:
			if re.match("[0-9]", value) is None:
				sys.exit('error: Invalid value in map')
			i += 1

	j = 0
	for index in check_len_line:
		if j != 0:
			if index != tmp:
				print('error: All your line have not the same lenght')
				return (False)
		tmp = index
		if len(puzzle) != check_len_line[0]:
			print('error: Map is not a square')
			return (False)
		if check_len_line[0] != int(var_length[0]) or int(var_length[0]) != len(puzzle):
			print('error: Length doesn\'t correspond the number at the top of the file.')
			return (False)
		j += 1
	return (True)




def parse(fileName):
	list_line_puzzle = []
	puzzle = []

	try:
		with open(fileName, 'r') as f:
			map_puzzle = f.readlines()
			for line in map_puzzle:
				comment = 0
				if line.find('#') > -1:
					index = line.index('#')
					comment = line[index:]
					line_puzzle = line[:index]
					line_split = re.sub('[\t|\s]+', ' ', line_puzzle)
					line_puzzle = line_split.split()
					list_line_puzzle.append(line_puzzle)
				else:
					line_puzzle = line.split()
					list_line_puzzle.append(line_puzzle)
			puzzle = [x for x in list_line_puzzle if x]
			len_top_file = puzzle[0]
			var_length.append(len_top_file[0])
			puzzle.pop(0)
			try:
				y = 0
				while (puzzle[y]):
					if set(puzzle[y]) & set(puzzle[y + 1]):
						sys.exit('error: You have put wrong number somewhere')
					y += 1
			except IndexError:
				pass

	except IOError as e:
		print("error: %s" % e)
		return (None)
	if not check_if_good(puzzle) or not check_all_number(puzzle):
		return (None)
	cast_to_int(puzzle)
	return (puzzle)