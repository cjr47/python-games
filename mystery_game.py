word_to_guess = list('dog')
board = list(len(word_to_guess) * '#')
print(board)

#return board with letter guess substitute


def guess_letter(word, counter):
    guess = input('Guess a letter ') 
    if guess not in word:
        counter += 1
        print(counter)
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
    return counter
        #guess_letter(word)
                #not needed: print(list(new_board))
                #for letter in word_to_guess:

def play_game(word):
    counter = 0
    while word != board and counter < 8:
        counter = guess_letter(word, counter)
    if word != board:
        print('Bummer! You ran out of tries!' + 'You Lost')
    else:
        print('Congrats!! You won!')

play_game(word_to_guess)

#guess_letter(word_to_guess)    
# maybe not use: for letter in enumerate(word_to_guess):
