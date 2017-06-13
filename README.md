# n-puzzle

The goal of this project is to solve the N-puzzle game using the __A*__ search algorithm or one of its variants.

## Example

_start position_

 5 | 2  | 9 
--| -- | --
3 | x | 1
8 | 7 | x

_final wanted position_

 1 | 2  | 3 
--| -- | --
4 | 5 | 6
7 | 8 | x

## Beginning
You start with a square board made up of N*N cells. One of these cells will be empty, the others will contain numbers, starting from 1, that will be unique in this instance of the puzzle.


Your search algorithm will have to find a valid sequence of moves in order to reach the
final state, a.k.a the "snail solution", which depends on the size of the puzzle.

