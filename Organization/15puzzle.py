import numpy
import math


# ________________solve_anal_project
# 0..3 to 0..15
# def XYtolin(X, Y):
#  N = 4
#  return Y*N + X


# 0..15 to 0..3
def getXY(lin):
    N = 4
    y = int(math.floor(lin / N))
    x = lin % N
    return x, y


# return empty puzzle (matrix from 1 to 16 (0))
def create_puz():
    arr = numpy.arange(1, 17)
    arr[15] = 0
    blank = 15
    return arr.reshape(4, 4), blank


# scramble matrix with string like slidysim
def scramble_puz(puzzle, scramble):
    blank = 15
    arr = tuple([int(a) for x in scramble.split("/") for a in x.split()])
    for idd, el in enumerate(arr):
        if el == 0:
            blank = idd
        x, y = getXY(idd)
        puzzle[y, x] = el
    return puzzle, blank


# do move, not check if possible, blank 0 id of empty, move - RULD
def move(puzzle, blank, move):
    xb, yb = getXY(blank)
    N = 4
    if move == "R":
        puzzle[yb, xb] = puzzle[yb, xb - 1]
        puzzle[yb, xb - 1] = 0
        blank -= 1
    if move == "L":
        puzzle[yb, xb] = puzzle[yb, xb + 1]
        puzzle[yb, xb + 1] = 0
        blank += 1
    if move == "D":
        puzzle[yb, xb] = puzzle[yb - 1, xb]
        puzzle[yb - 1, xb] = 0
        blank -= N
    if move == "U":
        puzzle[yb, xb] = puzzle[yb + 1, xb]
        puzzle[yb + 1, xb] = 0
        blank += N
    return puzzle, blank


# do moves sequence, like RULD... string, Null if whatever is wrong
def doMoves(puzzle, blank, moves):
    try:
        for i in moves:
            puzzle, blank = move(puzzle, blank, i)
        return puzzle, blank
    except:
        return None, None


# returns true if puzzle is solved
def checkSolved(puzzle):
    s, _ = create_puz()
    return numpy.array_equal(puzzle, s)


# get slidysim style scramble from array
def toScramble(puzzle):
    scr = ""
    for i in puzzle:
        for j in i:
            scr += str(j) + " "
        scr = scr[:-1] + "/"
    return scr[:-1]


mypuz, blank = create_puz()
mypuz, blank = scramble_puz(mypuz, "4 5 11 2/7 10 14 1/8 15 9 12/6 3 0 13")
print(toScramble(mypuz))
mypuz, _ = doMoves(mypuz, blank,
                   "LDRRULDRRDLLLURRDRDLLULURDRRUULDLDRDLLURRRULLDRRDLLLUUU")
print(checkSolved(mypuz))
