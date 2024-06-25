# hangman
import random
import hangman_words
import hangman_art

words = ["copper", "coffee", "doctor"]

chosen_word = random.choice(hangman_words.word_list)


print(hangman_art.logo)


display = []
word_length = len(chosen_word)
for _ in range(len(chosen_word)):
    display += "_"
# print(chosen_word)
print(display)


lives = 6


end_of_game = False
while not end_of_game:
    print("LIVES REMAINING : ", lives)
    guess = input("GUESS A LETTER : ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOOSE")
            print("THE WORD WAS : ",chosen_word)
    print(display)

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

    print(hangman_art.stages[lives])
