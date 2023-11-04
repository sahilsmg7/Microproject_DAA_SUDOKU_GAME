def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def is_valid_move(board, row, col, num):
    # Check the row
    if num in board[row]:
        return False

    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 grid
    row_start, col_start = 3 * (row // 3), 3 * (col // 3)
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def main():
    board = [[0 for _ in range(9)] for _ in range(9)]

    print("Enter the Sudoku puzzle one row at a time, use '0' for empty cells.")
    for i in range(9):
        row = input(f"Enter row {i + 1}: ")
        for j in range(9):
            board[i][j] = int(row[j])

    print("\nInput Sudoku puzzle:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku puzzle:")
        print_board(board)
    else:
        print("\nNo solution exists for the given puzzle.")

if __name__ == "__main__":
    main()
