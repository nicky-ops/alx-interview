#!/usr/bin/python3
'''
Implementing the N queens puzzle
'''
import sys


def main():
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

    solutions = []
    solve_nqueens(N, [], solutions)

    for solution in solutions:
        print(solution)


def solve_nqueens(N, board, solutions):
    row = len(board)
    if row == N:
        solutions.append(board)
        return
    for col in range(N):
        if is_valid_move(board, row, col):
            solve_nqueens(N, board + [[row, col]], solutions)


def is_valid_move(board, row, col):
    for r, c in board:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


if __name__ == "__main__":
    main()
