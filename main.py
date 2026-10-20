from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won
)

print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")

play_again = "yes"

# Repeat the game when the player chooses yes.
while play_again == "yes":
    secret_word = choose_word()
    previous_guesses = []
    won = False

    # Allow six valid guesses.
    for attempt in range(1, 7):
        print(f"\nAttempt {attempt} of 6")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("Congratulations! You solved the puzzle.")
            won = True
            break

    if not won:
        print(f"The secret word was: {secret_word}")

    play_again = input(
        "\nWould you like to play again? Type yes or no: "
    ).strip().lower()

print("Thanks for playing!")