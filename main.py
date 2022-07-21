import random

COMPUTER = None
USER = None


def computer_hack(user_pick, computer_pick):
    # this game can expand and avoid random move to check what first two pick user has have
    # every two numbers from data can computer change with third to stop users domination :D
    pass


def calculate_score(user, computer_num):
    # winning combination
    data = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for char in data:
        # if sum(user) == sum(char):
        #     if user == char:
        #         print("USER EASY WIN!")
        #         return True
        # elif sum(computer_num) == sum(char):
        #     if computer_num == char:
        #         print("COMPUTER EASY WIN")
        #         return True
        if len(user) == 3:
            # we need first winner with three picks
            # compare winning set with user or computer picks
            # then transform set to list to again check current char compare to comp or user pick lists
            user_set = set(char).intersection(user)
            new_user = list(user_set)
            if len(new_user) == 3:
                if new_user == char:
                    print("USER IS SMART")
                    return True

        elif len(computer_num) == 3:
            comp = set(char).intersection(computer_num)
            new_comp = list(comp)
            if len(new_comp) == 3:
                if new_comp == char:
                    print("USER IS NOT GOOD ENOUGH")
                    return True


display = []
# put positions in display to manipulate
for char in range(9):
    display += "⬜"


def tic_tac_toe():

    is_game = True
    user_pick = []
    computer_pick = []

    while is_game:

        user_choice = int(input("pick position for your sign: from 1-9: "))

        # computer pick random number
        computer_choice = random.randint(0, 8)
        print(computer_choice)
        # loop runs till found empty positions
        while user_choice == computer_choice or computer_choice in user_pick or computer_choice in computer_pick:
            computer_choice = random.randint(0, 8)
            # if len(computer_pick) == 4:
            #     print("POKIDAO SI NEO")
            #     break

        # we expand our user pick list to compare with winners
        user_pick.append(user_choice)
        # we have mark firs position in display
        display[user_choice] = USER

        computer_pick.append(computer_choice)
        display[computer_choice] = COMPUTER

        user_pick.sort()
        computer_pick.sort()

        #create table for correct tic tac toe visuelation
        char = ""
        for data in range(len(display)):
            if data % 3 == 0:
                char += "\n......\n"
            char += display[data]
            char += "|"

        print(char)
        # return from function with track of game
        final_result = calculate_score(user_pick, computer_pick)
        if final_result:
            is_game = False
            print("GOOD GAME")
        elif not "⬜" in display:
            is_game = False
            print("TOUGH GAME")

# game function won't start till choose do you like to start game with key 'y'
# who you want to play fist, 'you' or 'comp'?
# pick your favorite sign and pick any number from 0 - 8 to fill your table and hope you can beat my pc
# random simulation :D

while input("WOULD YOU LIKE TO TRY MY TIC-TAC-TAE?!") == "y":
    first_play = input("Who you want to play first? you or comp?")
    pick = input("what sign you choose? 'X' or 'O'?")
    if pick == "X":
        USER = pick
        COMPUTER = "O"
    else:
        USER = "O"
        COMPUTER = "X"
    if first_play == "comp":
        computer_choice = random.randint(0, 8)
        display[computer_choice] = COMPUTER
        tic_tac_toe()
    else:
        tic_tac_toe()
