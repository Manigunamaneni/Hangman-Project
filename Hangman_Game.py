import random
word_list = ["mani","chandu","surya","vishnu"]
lives=6
choose_word = random.choice(word_list)
print(choose_word)
placeholder=""
word_length = len(choose_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)
game_over = False
correct_letters=[]
while not game_over:
    print(f"************{lives}/6 lives left*****************")
    guess = input("Guess a letter: ").lower()
    display=""
    for letter in choose_word:
        if letter == guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in choose_word:
        lives-=1
        if lives==0:
            game_over=True
            print(f"***************IT WAS {choose_word}You lose!***************")

    if "_" not in display:
        game_over = True
        print("*******************you win******************")
