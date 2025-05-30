import random

words = ["python", "hangman", "programming", "computer", "developer"]

secret_word = random.choice(words)

attempts = 6

guessed_letters = []

display_word = ["_" for _ in secret_word]

print("Welcome to Hangman!")
print("The word contains", len(secret_word), "letters.")
print("You have", attempts, "attempts to guess the word.")
print("The hidden word is: ", " ".join(display_word))
print("-" * 30)

while attempts > 0 and "_" in display_word:
    print("\nGuessed letters so far:", ", ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Error: Please enter a single letter (A-Z).")
        continue

    if guess in guessed_letters:
        print("You have already guessed this letter. Try another one.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct! The letter is in the word.")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print("Sorry, the letter is not in the word. You have", attempts, "attempts remaining.")

    print("Current word: ", " ".join(display_word))
    print("-" * 30)

if "_" not in display_word:
    print("\nCongratulations! You have guessed the word successfully!")
    print("The word was:", secret_word.upper())
else:
    print("\nUnfortunately, you ran out of attempts. You lost!")
    print("The word was:", secret_word.upper())
    print("Try again!")
