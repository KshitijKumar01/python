import random
import hangman_words 
import hangman_art
from replit import clear

lives = 6

# choosing the random word from the word list
chosen_wrod = random.choice(hangman_words.word_list)
print(chosen_wrod)

#creating the empty list for storing the blanks and replacing the blanks with the letters 
display = []
for _ in range(len(chosen_wrod)):
    display += "_"
# print(f"{' '.join(display)}")

# while loop for repeating the code for choosing the word
end_of_game = False

print(hangman_art.logo)
while not end_of_game:

    guess = input("Guess a letter : ").lower()
    clear()

    if(guess in display):
        print(f"You have already gussed {guess}")

    for position in range(len(chosen_wrod)):
        letter = chosen_wrod[position]
        if(letter == guess):
            display[position] = letter
    
    if guess not in chosen_wrod:
        print(f"you gussed {guess}, that's not in the word. YOu lose the life.")
        lives -= 1
        if(lives == 0):
            end_of_game = True
            print("You Lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])
        