from functions import checkifwinner, checkifboardfull, update_board, ask_player, draw_board 
# Tic Tac Toe
# Setting up Game

while True:
    CurrentBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    CurrentPlayer = 1 # Can be 1 or 2

    draw_board(CurrentBoard)

    while True:
        position_response = ask_player(CurrentPlayer)

        value_in_position = CurrentBoard[position_response - 1]

        while value_in_position != ' ':
            print("This space isn't free!!! >:(") 
            position_response = ask_player(CurrentPlayer)
            value_in_position = CurrentBoard[position_response - 1]
        
        update_board(CurrentPlayer, position_response, CurrentBoard)

        draw_board(CurrentBoard)

        # check if there's a winner
        iswinner = checkifwinner(CurrentBoard, CurrentPlayer)
        if iswinner:
            print("Player " + str(CurrentPlayer) + " Wins!!! :D")
            break

        # check if a draw
        isboardfull = checkifboardfull(CurrentBoard)
        if isboardfull:
            print("It's a Draw!!")
            break

        if CurrentPlayer == 1:
            CurrentPlayer = 2
        else: 
            CurrentPlayer = 1   
    print("Would you like to play again? Y/N")
    player_response = input()
    if player_response.lower() == "n":
        break

