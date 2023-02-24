from os import system
import random
from asciiarts import hangman_logo
from asciiarts import stages
from shabdkosh import word_list

print(hangman_logo)
random_word = random.choice(word_list)
blank_word = []

for letter in random_word:
    blank_word += "_"
game_over = False
lives = 6
print(f"Psst! Guessed word is: {random_word}.")

while not game_over:
    guess = input("Guess a letter:\n").lower()
    system('clear')
    for pos in range(0, len(random_word)):
        letter = random_word[pos]
        if guess == letter:
            if guess in blank_word:
                print(f"You've already guessed {letter}, try a different one.")
            blank_word[pos] = letter
    if guess not in random_word:
        print("Oops! The guessed letter is not in the word.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            game_over = True
    print("Guessed word: " + ' '.join(blank_word))

    if "_" not in blank_word:
        print("You win.")
        game_over = True

    print(stages[6 - lives])
