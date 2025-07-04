def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n, solutions, iteracoes):
    iteracoes[0] += 1  # Contador de chamadas recursivas (iterações)

    if row == n:
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions, iteracoes)
            board[row][col] = 0  # backtrack

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    iteracoes = [0]  # Usamos uma lista para passar por referência
    solve_n_queens(board, 0, n, solutions, iteracoes)

    print(f"\nTotal de iterações (chamadas recursivas): {iteracoes[0]}")
    print(f"Número total de soluções para {n} rainhas: {len(solutions)}\n")

    return solutions

# Exemplo de uso:
n = 5
sols = n_queens(n)
for sol in sols:
    print_board(sol)
