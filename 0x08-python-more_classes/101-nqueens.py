#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col, N):
    # check if the column is safe
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check if the top-left diagonal is safe
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check if the top-right diagonal is safe
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, N):
    # base case: if all rows are checked, return True
    if row == N:
        return True

    # try placing the queen in all columns of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # place the queen in (row, col)
            board[row][col] = 1
            # try solving the rest of the board
            if solve_nqueens(board, row + 1, N):
                return True
            # backtrack: remove the queen from (row, col)
            board[row][col] = 0

    return False


def main():
    # check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # initialize the board
    board = [[0] * N for _ in range(N)]

    # solve the N queens problem
    if not solve_nqueens(board, 0, N):
        print("Solution does not exist")
    else:
        # print the solutions
        for row in board:
            print(row)


if __name__ == "__main__":
    main()
