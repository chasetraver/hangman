
import json
import requests


def drawhangman(wronganswers):
    # makes picture of "hanged man"
    head, chest, arm1, arm2, leg1, leg2 = (" ", " ", " ", " ", " ", " ")
    if wronganswers < 6:
        head = "O"
    if wronganswers < 5:
        chest = "|"
    if wronganswers < 4:
        arm1 = "/"
    if wronganswers < 3:
        arm2 = '\\'
    if wronganswers < 2:
        leg1 = "/"
    if wronganswers < 1:
        leg2 = "\\"

    print(" -----------")
    print(" |         |")
    print(" |         |")
    print(f" |         {head}")
    print(f" |        {arm1}{chest}{arm2}  ")
    print(f" |        {leg1} {leg2} ")
    print(" |")
    print("----")


startwronganswers = 6
game = True
print(f"Welcome to Hangman! I've selected a random word. Guess a letter to reveal it, or the whole word to win. "
      f"\nAfter {startwronganswers} wrong answers, you lose.")

while game:
    wronganswers = startwronganswers

    # get random word from random word api
    data = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    word = data.json()[0]

    guesses = []

    # loop till no wronganswers are remaining
    while wronganswers > 0:
        unknown = 0

        for letter in word:
            if letter in guesses:
                print(letter, end="")
            else:
                print("_", end="")
                unknown += 1

        print("\n")

        if unknown == 0:
            print("You win!")

            break

        guess = ""
        if len(guess) < 1:
            if len(guesses) > 0:
                print("previous guesses:", end="")
            for letter in guesses:
                print(letter, end="")
            print("\n")
            guess = input("Guess a character or enter the correct word: ")
            # checks if player inputted one letter or multiple
            if len(guess) > 1:
                if guess == word:
                    print(f"Correct! It is {word}!")
                    print("You win!")
                    break
            else:
                if guess in guesses:
                    print("You already guessed that! Try again.")
                else:
                    # adds letter to previous guesses
                    guesses.extend(guess)

        # if player guessed a letter not in the word, or if the player guesses a string that is not the word
        if guess not in word and guess != word:
            wronganswers -= 1

            print("Wrong")
            drawhangman(wronganswers)
            print(f"You have {wronganswers} wrong guesses left!")

            if wronganswers == 0:
                print("You Lose :(")
                print(f"The correct answer is {word}")

    # Restart game
    while True:
        response = input("Would you like to play again? Y/N?")
        response = response.upper()
        if response == "N":
            game = False
            print("Ok, thanks for playing!")
            break
        elif response == "Y":
            print("Ok, I'll pick another word.")
            break
        else:
            print("I'm sorry, I didn't understand that.")


