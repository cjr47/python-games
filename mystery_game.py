        #guess_letter(word)
                #not needed: print(list(new_board))
                #for letter in word_to_guess:
 # line 15 assigns indexes to each character
            # range determines the collection of numbers in order in word_to_guess
            # index is the position for each letter
import random
easy, normal, difficult = [], [], []

# def computerword(word):
with open('words.txt', 'r') as reader:
    word_list = reader.read().splitlines()
    print(len(word_list))
word = random.choice(0, len(word_list))
   
    # if word <=5:
    #     word == easy[]
    # elif word >5 + <=8:
    #     word == normal[]
    # else word >9:
    #     word == difficult[]
    # return

word_to_guess = list('dog')
board = list(len(word_to_guess) * '#')
print(board)

def guess_letter(word, counter):
    guess = input('Guess a letter ') 
    if guess not in word:
        counter += 1
        print(counter)
        print('Not in word :( Guess again!!')      
    else:    
        for index in range(len(word_to_guess)):
            if guess == word_to_guess[index]:
                    board[index] = guess
                    print(board)   
    return counter

def play_game(word):
    counter = 0
    while word != board and counter < 8:
        counter = guess_letter(word, counter)
    if word != board:
        print('Bummer! You ran out of tries!' + 'You Lost')
    else:
        print('Congrats!! You won!')

play_game(word_to_guess)

