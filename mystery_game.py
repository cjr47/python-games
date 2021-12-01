word_to_guess = 'dog'
board = len(word_to_guess) * '#'
print(board)
guess = input('Guess a letter ')
def guess_letter(letter, word):
    if letter not in word:
        print('Not in word :( Guess again!!')
    else: 
        print('Congrats!!')
        for letter in word_to_guess:
            pass      

guess_letter(guess, word_to_guess)    
