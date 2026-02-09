import random

def play_hangman():
    # 1. Predefined list of 5 words
    words = ["python", "code", "loops", "game", "list"]
    chosen_word = random.choice(words)
    word_display = ["_" for _ in chosen_word] # Create list of underscores
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    # 2. Game Loop
    while attempts > 0 and "_" in word_display:
        print("\n" + " ".join(word_display))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        # Basic validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that!")
            continue

        guessed_letters.append(guess)

        # 3. Check guess
        if guess in chosen_word:
            print(f"Good job! {guess} is in the word.")
            # Update the display
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess
        else:
            print(f"Sorry, {guess} is not there.")
            attempts -= 1

    # 4. Game Over conditions
    if "_" not in word_display:
        print(f"\nYou won! The word was: {chosen_word}")
    else:
        print(f"\nGame Over! The word was: {chosen_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()