**HOW TO**

1. "source start.sh"
2. python srcs/npuzzle.py [puzzle_file]

# n-puzzle

The goal of this project is to solve the N-puzzle game using the __A*__ search algorithm or one of its variants.

## Example

**X** represents the empty cell

_start position_

 5 | 2  | 9 
--| -- | --
3 | **X** | 1
8 | 7 | 4

_final wanted position_

 1 | 2  | 3 
--| -- | --
4 | 5 | 6
7 | 8 | **X**

## Beginning
You start with a square board made up of N*N cells. One of these cells will be empty, the others will contain numbers, starting from 1, that will be unique in this instance of the puzzle.


Your search algorithm will have to find a valid sequence of moves in order to reach the
final state, a.k.a the "snail solution", which depends on the size of the puzzle.


_notes_

Greedy A* is described here https://en.wikipedia.org/wiki/A*_search_algorithm#Relations_to_other_algorithms

