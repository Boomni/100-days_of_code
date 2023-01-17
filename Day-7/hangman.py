import random

from hangman_words import word_list

chosen = random.choice(word_list).lower()
length = len(chosen)

end = False
lives = 6

from hangman_art import logo
print(logo)

from hangman_instruction import instructions
print(instructions)

display = []
for _ in range(length):
    display.append("_")

while not end:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already guessed", guess)

    #Check guessed letter
    for position in range(length):
        letter = chosen[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen:
        print("You guessed", guess, "that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end = True
            
    print(f"{' '.join(display).upper()}")

    #Check if user has got all letters.
    if "_" not in display:
        end = True
    
    from hangman_art import stages
    print(stages[lives])

if lives == 0:
        print("The word was", chosen.upper())
        print("You lose!")
if "_" not in display:
        print("You win!")
print("Game Over!")
