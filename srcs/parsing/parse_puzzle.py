import re
import sys

var_length = []

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
			sys.exit('error: Invalid value')


def check_if_good(puzzle):
	check_len_line = []
	for tab in puzzle:
		i = 0
		check_len_line.append(len(tab))
		for value in tab:
			# print("mdr la valeur comme le raton: %s" % value)
			if re.match("[0-9]", value) is None:
				sys.exit('error: Invalid value in map')
			i += 1

	j = 0
	for index in check_len_line:
		if j != 0:
			if index != tmp:
				sys.exit('error: All your line have not the same lenght')
		tmp = index
		if len(puzzle) != check_len_line[0]:
			sys.exit('error: Map is not a square')
		if check_len_line[0] != int(var_length[0]) or int(var_length[0]) != len(puzzle):
			sys.exit('error: Length doesn\'t correspond the number at the top of the file.')
		j += 1




def parse():
	final = []

	try:
		map_name = str(sys.argv[1])
	except IndexError:
		print("error: Please enter a map")
		sys.exit(1)
	try:
		with open(map_name) as f:
			map_puzzle = f.readlines()
			for line in map_puzzle:
				comment = 0
				if line.find('#') > -1:
					index = line.index('#')
					comment = line[index:]
					line_puzzle = line[:index]
					line_split = re.sub('[\t|\s]+', ' ', line_puzzle)
					mdr_g_chercher_pour_rien = line_split.split()
					line_puzzle = mdr_g_chercher_pour_rien
					final.append(line_puzzle)
				else:
					line_puzzle = line.split()
					final.append(line_puzzle)
				# print("line_puzzle: %s" % line_puzzle)
				# print("comment: %s" % comment)
				# print("line_split: %s" % line_split)
			puzzle = [x for x in final if x]
			len_top_file = puzzle[0]
			var_length.append(len_top_file[0])
			puzzle.pop(0)
			try:
				y = 0
				while (puzzle[y]):
					if set(puzzle[y]) & set(puzzle[y + 1]):
						# print(set(puzzle[y]) & set(puzzle[y + 1]))
						sys.exit('error: You have put wrong number somewhere')
					y += 1
			except IndexError:
				pass

	except IOError as e:
		print("error: %s" % e)

	return(puzzle)

mdr_le_puzzle = parse()
mdr_le_vrai_puzzle = check_if_good(mdr_le_puzzle)
mdr_un_autre_puzzle = check_all_number(mdr_le_puzzle)
# print(mdr_un_autre_puzzle)