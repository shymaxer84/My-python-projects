import random

words = ['phyton', 'java', 'selenium']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores

attempts = 8  # Number of allowed attempts

print("Wellcome to Hangman")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter:").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # reveal letter
    else:
        print("That letter doesn't appear in the word")
        attempts += 1
# Game conclusion
if '_' not in word_display:
    print("You guessed the word!")
    print(' '.join(word_display))
    print("you survived!")
else:
    print("You ran out of attemps. The word was" + chosen_word)
    print("you lost")
