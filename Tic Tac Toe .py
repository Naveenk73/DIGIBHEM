def display_board(board):
    print( board[0] + "  | "+ board[1] + "  | "+ board[2] )
    print("------------")
    print( board[3] + "  | "+ board[4] + "  | "+ board[5] )
    print("------------")
    print( board[6] + "  | "+ board[7] + "  | "+ board[8] )
    
def check_winning_conditions(board):
    player_1 = "X"
    player_2 = "O"
    if board[0]==board[1]==board[2]==player_1 or board[0]==board[1]==board[2]==player_2:  
        return True
    elif board[3]==board[4]==board[5]==player_1 or board[3]==board[4]==board[5]==player_2:
        return True  
    elif board[6]==board[7]==board[8]==player_1 or board[6]==board[7]==board[8]==player_2:
        return True  
    elif board[0]==board[3]==board[6]==player_1 or board[0]==board[3]==board[6]==player_2: 
        return True  
    elif board[1]==board[4]==board[7]==player_1 or board[1]==board[4]==board[7]==player_2:
        return True  
    elif board[2]==board[5]==board[8]==player_1 or board[2]==board[5]==board[8]==player_2:
        return True  
    elif board[0]==board[4]==board[8]==player_1 or board[0]==board[4]==board[8]==player_2: 
        return True  
    elif board[2]==board[4]==board[6]==player_1 or board[2]==board[4]==board[6]==player_2:
        return True  
    else:
        return False

def inp(board):
    try:
        x = int(input("Enter the position 1-9 ==> "))
        if x < 1 or x > 9:
            print("Please enter a number between 1 and 9.")
            return inp(board)
        if board[x-1] != "-":
            print("That spot is already taken.")
            return inp(board)
        return x
    except ValueError:
        print("Invalid input. Please enter a number.")
        return inp(board)

def play_game():
    board = ["-"] * 9
    player1 = input("Enter the player 1 name ==> ")
    player2 = input("Enter the player 2 name ==> ")
    display_board(board)

    for i in range(9):
        if i % 2 == 0:
            print(f"{player1} (X)'s turn:")
            x = inp(board)
            board[x - 1] = "X"
        else:
            print(f"{player2} (O)'s turn:")
            x = inp(board)
            board[x - 1] = "O"

        display_board(board)

        if check_winning_conditions(board):
            winner = "X" if i % 2 == 0 else "O"
            print(f"🎉 Player {winner} wins! 🥳")
            break
    else:
        print("🤝 It's a tie!")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break
main()
