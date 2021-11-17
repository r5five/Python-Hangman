import random

stages = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(display)


end_of_game = False
while not end_of_game:
    guess = input("Choose a letter: ").lower()

    for postion in range(word_length):
        letter = chosen_word[postion]
        if letter == guess:
            display[postion] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")
