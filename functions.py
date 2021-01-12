def checkifwinner(board, player):
    player_symbol = "x"
    if player == 2:
        player_symbol = "o"

    # check rows
    if (board[0] == player_symbol) and (board[1] == player_symbol) and (board[2] == player_symbol):
        return True

    if (board[3] == player_symbol) and (board[4] == player_symbol) and (board[5] == player_symbol):
        return True
    
    if (board[6] == player_symbol) and (board[7] == player_symbol) and (board[8] == player_symbol):
        return True

    # check columns
    if (board[0] == player_symbol) and (board[3] == player_symbol) and (board[6] == player_symbol):
        return True
    
    if (board[1] == player_symbol) and (board[4] == player_symbol) and (board[7] == player_symbol):
        return True

    if (board[2] == player_symbol) and (board[5] == player_symbol) and (board[8] == player_symbol):
        return True

    # check diagonal
    if (board[0] == player_symbol) and (board[4] == player_symbol) and (board[8] == player_symbol):
        return True
    if (board[2] == player_symbol) and (board[4] == player_symbol) and (board[6] == player_symbol):
        return True

    return False

def checkifboardfull(board):
    for value in board:
        if value == " ":
            return False
    return True

def update_board(player, player_response, any_board):
    player_symbol = "x"
    if player == 2:
        player_symbol = "o"
    any_board[player_response -1] = player_symbol

def ask_player(player):
    print("Player " + str(player))
    print("Please select an empty space between 1 and 9: ")

    # input 
    player_response = int(input())
    return player_response

def draw_board(board):
  print("___________________")
  print("|     |     |     |")
  print("|  " + board[0] + "  |  " + board[1] + "  |  " + board[2] +"  |")
  print("|     |     |     |")
  print("|-----------------|")
  print("|     |     |     |")
  print("|  " + board[3] + "  |  " + board[4] + "  |  " + board[5] +"  |")
  print("|     |     |     |")
  print("|-----------------|")
  print("|     |     |     |")
  print("|  " + board[6] + "  |  " + board[7] + "  |  " + board[8] +"  |")
  print("|     |     |     |")
  print("|-----------------|")