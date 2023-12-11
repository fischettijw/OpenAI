import tkinter as tk

root = tk.Tk()
root.title("Tic-Tac-Toe")

turn = "X"
board = [" "] * 9

def button_clicked(index):
    global turn
    if board[index] == " ":
        board[index] = turn
        turn = "O" if turn == "X" else "X"
    update_board()
    check_for_victory()

def check_for_victory():
    for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[a] == board[b] == board[c] != " ":
            show_victory(board[a])
            return
    if " " not in board:
        show_victory("tie")

def show_victory(player):
    global root
    win_message = tk.Label(root, text=f"{player} wins!" if player != "tie" else "It's a tie!")
    win_message.grid(row=3, column=0, columnspan=3)
    for i in range(9):
        buttons[i]["state"] = "disabled"

def update_board():
    for i in range(9):
        buttons[i]["text"] = board[i]

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 24), height=4, width=8, command=lambda index=i: button_clicked(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()




root = tk.Tk()
root.title("Tic-Tac-Toe")

turn = "X"
board = [" "] * 9

def button_clicked(index):
    global turn
    if board[index] == " ":
        board[index] = turn
        turn = "O" if turn == "X" else "X"
    update_board()
    check_for_victory()

def check_for_victory():
    for a, b, c in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
        if board[a] == board[b] == board[c] != " ":
            show_victory(board[a])
            return
    if " " not in board:
        show_victory("tie")

def show_victory(player):
    global root
    win_message = tk.Label(root, text=f"{player} wins!" if player != "tie" else "It's a tie!")
    win_message.grid(row=3, column=0, columnspan=3)
    for i in range(9):
        buttons[i]["state"] = "disabled"

def update_board():
    for i in range(9):
        buttons[i]["text"] = board[i]

buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 24), height=4, width=8, command=lambda index=i: button_clicked(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

root.mainloop()
