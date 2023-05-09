# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random

# Initialize

with open('wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]
allowed_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word, it was {word}")
else:
    print(f"You are dead. The word was {word}")
