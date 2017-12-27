#8. Write a function game() number-guessing game, that takes 2 int parameters defining the range.
# Using random.randint(A, B) generate random int from the range. While user input isn't equal that number, print
# "Try again!". If user guess the number, congratulate him and exit. (use raw_input())

import random


def function_game(A,B):
    one = random.randint(A,B)
    user_choise = input("Please, enter the number:")
    try:
        user_choise = int(user_choise)
    except:
        print("You enter invalid value, try again with some number.")
        function_game(A, B)

    if isinstance(user_choise, int):
        if one == user_choise:
            print("Congratulate!")
            exit()
        else:
            print("Try again!")
            function_game(A, B)
    else:
        print("This is not a number, try again!")
        function_game(A, B)

function_game(1,2)
