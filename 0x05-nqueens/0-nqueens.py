#!/usr/bin/python3
'''
Implementing the N queens puzzle
'''
import sys


def solveNQueens():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if int(N) < 4:
        print("N must be at least 4")
        sys.exit(1)
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = [["."] * N for i in range(N)]

    def backtrack(r: int):
        if r == N:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(N):
            if c in col or (r + c) in posDiag or (r-c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    print(res)

solveNQueens()
