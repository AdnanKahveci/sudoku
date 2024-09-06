import tkinter as tk
import numpy as np
import random
import time

# Sudoku çözümleyici
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            update_gui(board)  # GUI'yi güncelle
            root.update()
            time.sleep(0.5)  # Her adım arasında bekle
            if solve_sudoku(board):
                return True
            board[row][col] = 0
            update_gui(board)  # GUI'yi güncelle
            root.update()
            time.sleep(0.5)  # Her adım arasında bekle
    return False

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def fill_board(board):
    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve(board)
    return board

def generate_sudoku():
    board = np.zeros((9, 9), dtype=int)
    board = fill_board(board)
    num_cells_to_remove = random.randint(20, 30)
    for _ in range(num_cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def update_gui(board):
    for row in range(9):
        for col in range(9):
            value = board[row][col]
            cell = cells[row][col]
            cell.delete(0, tk.END)
            if value != 0:
                cell.insert(0, str(value))
            cell.config(bg='lightgreen' if value != 0 else 'white')

def new_game():
    """Yeni bir Sudoku tahtası oluşturur ve GUI'yi günceller."""
    global sudoku_board
    sudoku_board = generate_sudoku()
    update_gui(sudoku_board)


def start_solving():
    solve_sudoku(sudoku_board)

# GUI oluşturma
root = tk.Tk()
root.title("Sudoku Çözümleyici")

frame = tk.Frame(root)
frame.pack()

cells = [[None for _ in range(9)] for _ in range(9)]

for row in range(9):
    for col in range(9):
        cell = tk.Entry(frame, width=3, font=('Arial', 18), borderwidth=2, relief='solid')
        cell.grid(row=row, column=col, padx=1, pady=1)
        cells[row][col] = cell

sudoku_board = generate_sudoku()
update_gui(sudoku_board)

# Çözüm butonu
solve_button = tk.Button(root, text="Çözümü Başlat", command=start_solving)
solve_button.pack(side=tk.LEFT, padx=20, pady=10)

# Yeni Oyun butonu
new_game_button = tk.Button(root, text="Yeni Oyun", command=new_game)
new_game_button.pack(side=tk.RIGHT, padx=20, pady=10)
root.mainloop()
