import random


def choose_word():
    # Use five-letter words without repeated letters.
    words = [
        "beach", "brain", "bread", "brick", "brush",
        "chair", "charm", "cloud", "dance", "dream",
        "drink", "earth", "field", "flame", "fruit",
        "ghost", "grape", "heart", "horse", "house",
        "juice", "knife", "light", "magic", "money",
        "night", "ocean", "plant", "river", "shark",
        "smile", "snake", "stone", "table", "water",
        "crane", "slate", "proud", "tiger", "whole"
    ]

    return random.choice(words)

def get_guess(previous_guesses):
    while True:
        guess = input("Enter a five-letter word: ").strip().lower()

        if len(guess) != 5:
            print("Your guess must be exactly five letters.")

        elif not guess.isalpha():
            print("Use letters only.")

        elif guess in previous_guesses:
            print("You already guessed that word.")

        else:
            return guess

def evaluate_guess(guess, secret_word):
    feedback = []

    for index in range(5):
        if guess[index] == secret_word[index]:
            feedback.append("G")

        elif guess[index] in secret_word:
            feedback.append("Y")

        else:
            feedback.append("-")

    return feedback

def display_guess(guess, feedback):
    print("Guess:   ", " ".join(guess))
    print("Feedback:", " ".join(feedback))


def has_won(guess, secret_word):
    return guess == secret_word