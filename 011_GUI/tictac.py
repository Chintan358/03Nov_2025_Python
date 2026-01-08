import tkinter as tk
from tkinter import messagebox
import random
import winsound

# ---------------- CONFIG ----------------
BG_LIGHT = "#f0f0f0"
BG_DARK = "#1e1e1e"
BTN_LIGHT = "#ffffff"
BTN_DARK = "#333333"
X_COLOR = "#ff5252"
O_COLOR = "#4fc3f7"

current_theme = "dark"
player = "X"
ai = "O"
game_over = False
difficulty = "Hard"

# ---------------- SOUND ----------------
def play_click():
    winsound.Beep(800, 100)

def play_win():
    winsound.Beep(1200, 300)

def play_draw():
    winsound.Beep(600, 300)

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Advanced Tic Tac Toe")
root.geometry("420x550")
root.resizable(False, False)

# ---------------- GAME STATE ----------------
board = [""] * 9
buttons = []

# ---------------- THEME ----------------
def apply_theme():
    bg = BG_DARK if current_theme == "dark" else BG_LIGHT
    btn = BTN_DARK if current_theme == "dark" else BTN_LIGHT

    root.config(bg=bg)
    title.config(bg=bg, fg="white" if current_theme == "dark" else "black")
    control_frame.config(bg=bg)

    for b in buttons:
        b.config(bg=btn, activebackground=btn)

def toggle_theme():
    global current_theme
    current_theme = "light" if current_theme == "dark" else "dark"
    apply_theme()

# ---------------- WIN CHECK ----------------
def check_winner(bd):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in wins:
        if bd[a] == bd[b] == bd[c] != "":
            return bd[a]
    return None

# ---------------- AI LOGIC ----------------
def minimax(bd, is_max):
    winner = check_winner(bd)
    if winner == ai:
        return 1
    if winner == player:
        return -1
    if "" not in bd:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if bd[i] == "":
                bd[i] = ai
                score = minimax(bd, False)
                bd[i] = ""
                best = max(best, score)
        return best
    else:
        best = 100
        for i in range(9):
            if bd[i] == "":
                bd[i] = player
                score = minimax(bd, True)
                bd[i] = ""
                best = min(best, score)
        return best

def ai_move():
    if difficulty == "Easy":
        move = random.choice([i for i in range(9) if board[i] == ""])

    elif difficulty == "Medium":
        for i in range(9):
            if board[i] == "":
                board[i] = ai
                if check_winner(board) == ai:
                    board[i] = ""
                    move = i
                    break
                board[i] = ""
        else:
            move = random.choice([i for i in range(9) if board[i] == ""])

    else:  # HARD
        best = -100
        move = None
        for i in range(9):
            if board[i] == "":
                board[i] = ai
                score = minimax(board, False)
                board[i] = ""
                if score > best:
                    best = score
                    move = i

    make_move(move, ai)

# ---------------- MOVE ----------------
def make_move(index, symbol):
    if board[index] == "" and not game_over:
        play_click()
        board[index] = symbol
        buttons[index].config(
            text=symbol,
            fg=X_COLOR if symbol == "X" else O_COLOR,
            relief="sunken"
        )

        winner = check_winner(board)
        if winner:
            play_win()
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            reset_game()
        elif "" not in board:
            play_draw()
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        elif symbol == player:
            root.after(300, ai_move)

# ---------------- RESET ----------------
def reset_game():
    global board, game_over
    board = [""] * 9
    game_over = False
    for b in buttons:
        b.config(text="", relief="raised")

# ---------------- UI ----------------
title = tk.Label(root, text="TIC TAC TOE", font=("Segoe UI", 22, "bold"))
title.pack(pady=10)

control_frame = tk.Frame(root)
control_frame.pack(pady=5)

tk.Button(control_frame, text="Toggle Theme", command=toggle_theme).grid(row=0, column=0, padx=5)
tk.Label(control_frame, text="Difficulty").grid(row=0, column=1)

diff = tk.StringVar(value="Hard")
tk.OptionMenu(control_frame, diff, "Easy", "Medium", "Hard",
              command=lambda v: globals().update(difficulty=v)).grid(row=0, column=2)

# ---------------- BOARD ----------------
board_frame = tk.Frame(root)
board_frame.pack(pady=20)

for i in range(9):
    btn = tk.Button(
        board_frame,
        text="",
        font=("Segoe UI", 24, "bold"),
        width=4,
        height=2,
        relief="raised",
        bd=5,
        command=lambda i=i: make_move(i, player)
    )
    btn.grid(row=i//3, column=i%3, padx=6, pady=6)
    buttons.append(btn)

apply_theme()
root.mainloop()
