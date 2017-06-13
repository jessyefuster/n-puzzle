import re
import sys

def parse():
	try:
		map_name = str(sys.argv[1])
	except IndexError:
		print("error: Please enter a map")
		sys.exit(1)
	try:
		with open(map_name) as f:
			map_puzzle = f.readlines()
			for line in map_puzzle:
				print(re.search('[0-9]', line))
	except IOError as e:
		print("error: {}".format(e))

parse()