#!/usr/bin/python3
import sys
"""Import a sys"""


def print_solution(board):
    """Print the board configuration as a list of positions of queens."""
    print(board)


def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N-Queens problem using backtracking."""
    def backtrack(board, row):
        if row == N:
            print_solution(board)
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1  # Backtrack

    board = [-1] * N
    backtrack(board, 0)


def main():
    """A method that starts the program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
