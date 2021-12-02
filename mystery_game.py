word_to_guess = list('dog')
board = list(len(word_to_guess) * '#')
print(board)

#return board with letter guess substitute


def guess_letter(word):
    guess = input('Guess a letter ') 
   
    if guess not in word:
            print('Not in word :( Guess again!!')      
    else: 
            # line 15 assigns indexes to each character
            # range determines the collection of numbers in order in word_to_guess
            # index is the position for each letter
            for index in range(len(word_to_guess)):
                if guess == word_to_guess[index]:
                    board[index] = guess
                    print(board)    
            #print('Congrats!! You guessed correctly')
            return 
        #guess_letter(word)
                #not needed: print(list(new_board))
                #for letter in word_to_guess:

def play_game(word):
    while word != board:
        guess_letter(word)

play_game(word_to_guess)

#guess_letter(word_to_guess)    
# maybe not use: for letter in enumerate(word_to_guess):
