# Tic-Tac-Toe Developer Solo Submission by Madalyn Mounts

def main():

    # Defining numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Defining stop_game
    stop_game = False

    # Printing new board
    x_input = "0"
    o_input = "0"
    print_board(x_input, o_input, numbers)

    # Starting the game
    while not we_have_a_winner(numbers):

        # x's turn
        print ()
        x_input = input(str("x's turn to choose a square (1-9): "))
        print_board(x_input, o_input, numbers)

        if stop_game == we_have_a_winner(numbers):
            # o's turn
            print ()
            o_input = input(str("o's turn to choose a square (1-9): "))
            print_board(x_input, o_input, numbers)



def print_board(x_input, o_input, numbers):
    """Print the board for the players to see where they've marked using user input and the numbers list
    Parameters:
        x_input: where the user playing as x wants to mark
        o_input: where the user playing as o wants to mark
        numbers: the list of numbers to put on the board
    Return: none"""

    # For x's turn
    if x_input == "1":
        numbers[0] = "x"

    elif x_input == "2":
        numbers[1] = "x"

    elif x_input == "3":
        numbers[2] = "x"
    
    elif x_input == "4":
        numbers[3] = "x"

    elif x_input == "5":
        numbers[4] = "x"

    elif x_input == "6":
        numbers[5] = "x"

    elif x_input == "7":
        numbers[6] = "x"

    elif x_input == "8":
        numbers[7] = "x"

    elif x_input == "9":
        numbers[8] = "x"

    # For o's turn
    if o_input == "1":
        numbers[0] = "o"
    
    elif o_input == "2":
        numbers[1] = "o"

    elif o_input == "3":
        numbers[2] = "o"
    
    elif o_input == "4":
        numbers[3] = "o"

    elif o_input == "5":
        numbers[4] = "o"

    elif o_input == "6":
        numbers[5] = "o"

    elif o_input == "7":
        numbers[6] = "o"

    elif o_input == "8":
        numbers[7] = "o"

    elif o_input == "9":
        numbers[8] = "o"

    # Print the board
    print (f"{numbers[0]}|{numbers[1]}|{numbers[2]}")
    print ("-+-+-")
    print (f"{numbers[3]}|{numbers[4]}|{numbers[5]}")
    print ("-+-+-")
    print (f"{numbers[6]}|{numbers[7]}|{numbers[8]}")

def we_have_a_winner(numbers):
    """Determines if one of the users has won the game by meeting one of the win conditions
    Parameters: 
        numbers: the list of numbers and markings from the players
    Return:
        True or False: determines if a win condition has been met or not"""

    # Win conditions
    if numbers[0] == "x" and numbers[1] == "x" and numbers[2] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[3] == "x" and numbers[4] == "x" and numbers[5] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[6] == "x" and numbers[7] == "x" and numbers[8] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[0] == "x" and numbers[3] == "x" and numbers[6] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[1] == "x" and numbers[4] == "x" and numbers[7] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[2] == "x" and numbers[5] == "x" and numbers[8] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[0] == "x" and numbers[4] == "x" and numbers[8] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[2] == "x" and numbers[4] == "x" and numbers[6] == "x":
        print ("x is the winner! Good game!")
        return True

    elif numbers[0] == "o" and numbers[1] == "o" and numbers[2] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[3] == "o" and numbers[4] == "o" and numbers[5] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[6] == "o" and numbers[7] == "o" and numbers[8] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[0] == "o" and numbers[3] == "o" and numbers[6] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[1] == "o" and numbers[4] == "o" and numbers[7] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[2] == "o" and numbers[5] == "o" and numbers[8] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[0] == "o" and numbers[4] == "o" and numbers[8] == "o":
        print ("o is the winner! Good game!")
        return True

    elif numbers[2] == "o" and numbers[4] == "o" and numbers[6] == "o":
        print ("o is the winner! Good game!")
        return True

    else: 
        for number in range(9):
            if numbers[number] != "x" and numbers[number] != "o":
                return False
        print ("It's a tie! Good game!")
        return True
    

if __name__ == "__main__":
    main()