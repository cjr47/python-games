# Write your blackjack game here.
import random
SUITS = ['♠️', '❤️', '♣️', '♦️']
SCORES = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',]

class Player:
    def __init__(self):
        self.name = input('What is your name? ')
        self.hand = []

    def show_hand(self):
        print(f'{self.name}\'s hand:')
        for card in self.hand:
            print(card)

    def __str__(self):
        return self.name

class Dealer:
    def __init__(self):
        self.hand = []

    def show_hand(self):
        print('Dealer hand:')
        for card in self.hand:
            print(card)

    def __str__(self):
        return 'Dealer'

class Cards:
    def __init__(self, rank, suit,):
        self.rank = rank
        self.suit = suit
        self.value = self.calculate_value(self.rank)

    def calculate_value(self, rank):
        values_dictionary = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'A':11}
        card_value = values_dictionary[rank]
        return card_value

    def __str__(self):
        return f'{self.rank} of {self.suit} '


class Deck:
    def __init__(self, suits, ranks):
            self.cards = []
            for suit in suits:
                for rank in ranks:
                    card = Cards(rank, suit)
                    self.cards.append(card)

    def show_cards(self):
        for card in self.cards:
            print(card)

    def draw_card(self):
        '''deals one card'''
        card_drawn = random.choice(self.cards)
        self.cards.remove(card_drawn)
        return card_drawn


class Game:
    def __init__(self, suit, rank):
        self.player = Player()
        self.dealer = Dealer()
        self.gamedeck = Deck(suit, rank)
        self.dealer_score = 0
        self.player_score = 0
   
    def deal_cards(self):
        print('The game is starting. Try to get 21 without going over. Dealer goes first. Goodluck!')
        for i in range(2):
            self.dealer.hand.append(self.gamedeck.draw_card())
            self.player.hand.append(self.gamedeck.draw_card())
        self.dealer.show_hand()
        self.player.show_hand()

    def hit(self,person):
        '''deal one card to player or dealer'''
        person.hand.append(self.gamedeck.draw_card())
        person.show_hand()

    def calculate_totals(self, dealer, player):
        self.dealer_hand_values = []
        self.player_hand_values = []
        for card in dealer.hand:
            self.dealer_hand_values.append(card.value)
        self.dealer_score = sum(self.dealer_hand_values)
        for card in player.hand:
            self.player_hand_values.append(card.value)
        self.player_score = sum(self.player_hand_values)

    def deal_dealer(self):   
        while self.dealer_score <= 17:
            self.hit(self.dealer)
            self.calculate_totals(self.dealer, self.player)
        else:
            print('The dealer\'s turn is over. The dealer is staying.')
            print(f'The dealer\'s score is {self.dealer_score}')

    def hit_or_stay(self):
        '''Ask for input from person for hit or stay'''
        while self.player_score < 21:
            choice = input('Your turn: Would you like to hit? y/n: ')
            if choice == 'n':
                print('You chose to stay')
                break
            self.hit(self.player)
            self.calculate_totals(self.dealer, self.player)
            print(f'Your score is now {self.player_score}')
        else:
            self.player.show_hand()
    
    def winner_loser(self):
        if self.dealer_score > 21:
            print('Dealer Busts - You Win!!')
        elif self.player_score > 21:
            print('You Bust - Dealer Wins')
        elif self.dealer_score == 21:
            print('Dealer has Black Jack')
        elif self.player_score == 21:
            print('Black Jack - You Win!!')
        elif self.dealer_score > self.player_score:
            print('Dealer Wins')
        elif self.dealer_score < self.player_score:
            print('You win!!')
        elif self.dealer_score == self.player_score:
            print('Draw - Play Again')

    def play_again(self):
        play_again_choice = input('Would you like to play again? y/n ')
        if play_again_choice == 'y':
            game = Game(SUITS, SCORES)
            game.deal_cards()
            game.deal_dealer()
            game.hit_or_stay()
            game.winner_loser()
            game.play_again()
        else:
            print('Game Ended')
        


game = Game(SUITS, SCORES)
game.deal_cards()
game.deal_dealer()
game.hit_or_stay()
game.winner_loser()
game.play_again()

    
 





        

