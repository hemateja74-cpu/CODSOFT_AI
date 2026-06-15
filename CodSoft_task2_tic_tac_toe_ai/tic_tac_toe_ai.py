import math

board = [" " for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == " "]

def winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(b[i] == player for i in combo) for combo in win_conditions)

def minimax(b, depth, is_maximizing):
    if winner(b, "O"): return 1
    if winner(b, "X"): return -1
    if " " not in b: return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            b[move] = "O"
            score = minimax(b, depth+1, False)
            b[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            b[move] = "X"
            score = minimax(b, depth+1, True)
            b[move] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in available_moves():
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    board[move] = "O"

print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
print_board()

while True:
    move = int(input("Enter your move (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Invalid move, try again.")
        continue

    print_board()
    if winner(board, "X"):
        print("You win!")
        break
    if " " not in board:
        print("It's a tie!")
        break

    ai_move()
    print("AI move:")
    print_board()
    if winner(board, "O"):
        print("AI wins!")
        break
    if " " not in board:
        print("It's a tie!")
        break
