# Tic-Tac-Toe Developer Solo Submission by Madalyn Mounts

def main():

    # Defining numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Defining win
    win = "no"

    # Printing new board
    x_input = "0"
    o_input = "0"
    print_board(x_input, o_input, numbers)

    # Starting the game
    while win == "no":

        # x's turn
        print ()
        x_input = input(str("x's turn to choose a square (1-9): "))
        print_board(x_input, o_input, numbers)

        # o's turn
        print ()
        o_input = input(str("o's turn to choose a square (1-9): "))
        print_board(x_input, o_input, numbers)

        # Check for winner
        win = we_have_a_winner(numbers)


def print_board(x_input, o_input, numbers):
    """"""

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
    """"""

    # Win conditions
    if numbers[0] == "x" and numbers[1] == "x" and numbers[2] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[3] == "x" and numbers[4] == "x" and numbers[5] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[6] == "x" and numbers[7] == "x" and numbers[8] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[0] == "x" and numbers[3] == "x" and numbers[6] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[1] == "x" and numbers[4] == "x" and numbers[7] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[2] == "x" and numbers[5] == "x" and numbers[8] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[0] == "x" and numbers[4] == "x" and numbers[8] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[2] == "x" and numbers[4] == "x" and numbers[6] == "x":
        print ("x is the winner! Good game!")
        win = "yes"

    elif numbers[0] == "o" and numbers[1] == "o" and numbers[2] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[3] == "o" and numbers[4] == "o" and numbers[5] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[6] == "o" and numbers[7] == "o" and numbers[8] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[0] == "o" and numbers[3] == "o" and numbers[6] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[1] == "o" and numbers[4] == "o" and numbers[7] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[2] == "o" and numbers[5] == "o" and numbers[8] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[0] == "o" and numbers[4] == "o" and numbers[8] == "o":
        print ("o is the winner! Good game!")
        win = "yes"

    elif numbers[2] == "o" and numbers[4] == "o" and numbers[6] == "o":
        print ("o is the winner! Good game!")
        win = "yes"
    
    #elif numbers[0] == "x" or numbers[0] == "o" and numbers[1] == "x" or numbers[1] == "o" and numbers[2] == "x" or numbers[2] == "o" and numbers[3] == "x" or numbers[3] == "o" and numbers[4] == "x" or numbers[4] == "o" and numbers[5] == "x" or numbers[5] == "o" and numbers[6] == "x" or numbers[6] == "o" and numbers[7] == "x" or numbers[7] == "o" and numbers[8] == "x" or numbers[8] == "o":
        #print ("It's a tie! Good game!") 
        #win = "yes"

    else:

        for number in range(9):
            if numbers[number] != "x" and numbers[number] != "o":
                win = "no"
        
            else:
                print ("It's a tie! Good game!")
                win = "yes"
    
    return win

if __name__ == "__main__":
    main()