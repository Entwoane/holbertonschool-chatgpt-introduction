#!/usr/bin/python3
import os
import signal
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    print("\nGame interrupted. Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def print_board(board):
    clear_screen()
    print("\n")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print("\n")

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Invalid input. Please enter a number between {valid_range[0]} and {valid_range[-1]}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Exiting...")
            sys.exit(0)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"Player {player}'s turn")
        
        while True:
            try:
                row = get_valid_input("Enter row (0, 1, or 2): ", range(0, 3))
                col = get_valid_input("Enter column (0, 1, or 2): ", range(0, 3))
                
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("That spot is already taken! Try again.")
            except (EOFError, KeyboardInterrupt):
                print("\nGame interrupted. Exiting...")
                sys.exit(0)
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        player = "O" if player == "X" else "X"

    while True:
        try:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again == 'y':
                tic_tac_toe()
            elif play_again == 'n':
                print("Thanks for playing!")
                sys.exit(0)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Exiting...")
            sys.exit(0)

def main():
    print("Welcome to Tic-Tac-Toe!")
    tic_tac_toe()

if __name__ == "__main__":
    main()
