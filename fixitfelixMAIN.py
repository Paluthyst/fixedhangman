import time

name = input("Hello Welcome to hangman whats your name?: ")
print("Hello", name, "are you ready to play?")
time.sleep(2)
print("Start guessing the word please")
time.sleep(0.5)
word = "secret"
guesses = ""
turns = 10

while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char)
        else:
            print("_____________________")
            failed += 1

        if failed == 0:
            print("You got a letter right")
            break

        guess = input("guess a character:")
        guess += guess

        if guess not in word:
            turns -= 1

            print("Wrong, You have", turns, "more guesses")

        if turns == 0:
            print("You Lose")
            break

