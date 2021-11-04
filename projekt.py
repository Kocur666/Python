import sys
import re

word = "kam"
used_letters = []
user_word = []
no_of_tries = 5


for _ in word:
    user_word.append("_")
def find_indexes(word, letter):
    global no_of_tries
    global user_word
    global used_letters
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def state_of_game():
    global no_of_tries
    global user_word
    global used_letters
    print()
    print("Used letters:", used_letters)
    print("Tries lasts:", no_of_tries)
    print("User word", user_word)
    print()

def validate_input():
    global letter
    while True:
        letter= str(input("Enter letter:"))
        if not re.match("^[a-z]{1}$", letter):
            print("Error! Only one a-z letter allowed.")
            continue
        break


def Main_game():
    global no_of_tries
    global user_word
    global used_letters
    global letter
    validate_input()
    used_letters.append(letter)

    found_indexes = find_indexes(word, letter)
    if len(found_indexes) == 0:
        print("You miss")
        no_of_tries -= 1
        if no_of_tries == 0:
            print("End of game")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter
        if "".join(user_word) == word:
            state_of_game()
            print("Wygrales !")
            print()
            print("Zwycieskie słowo to: ", "".join(user_word))
            #answer = input("Czy chcesz zagrać ponownie?")
            Zagraj_ponownie()
            #sys.exit(0)
    state_of_game()

def Zagraj_ponownie():
    global user_word
    global used_letters
    global no_of_tries
    used_letters.clear()
    user_word.clear()
    no_of_tries = 5
    for _ in word:
        user_word.append("_")
    answer = str(input("Do You want to play again? Y or N ?"))
    if answer == "Y":
        while True:
            Main_game()
    else:
        sys.exit(0)


while True:
    Main_game()