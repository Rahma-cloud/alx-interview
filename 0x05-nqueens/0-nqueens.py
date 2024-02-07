#!/usr/bin/python3

def is_safe(board, row, col, n):
    """ This function checks if there is a queen in the same column """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n, solutions):
    """ checks the location of the queen on the board and stores it """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)


def print_solutions(solutions):
    """ This function prints the solution in array form """
    for solution in solutions:
        print(solution)


def nqueens(n):
    """ This checks the value of n input """
    if not isinstance(n, int):
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    """ checks the number of argument passed """
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        exit(1)
