import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
'Queen': 10, 'King': 10, 'Ace': 10}

playing = True

#Card class

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

#Deck class

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has: ' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

#Hand class

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#Chips class

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

    def take_bet(chips):
        
        while True:
            try: 
                chips.bet = int(input('How many chips would like to bet? '))
            except ValueError:
                print('Sorry, a bet must be a number!')
            else:
                if chips.bet > chips.total:
                    print("Sorry, your bet can't exceed", chips.total)
                else:
                    break

    def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(deck,hand):
        global playing

        while True:
            ask = input("Would like to hit or stand? Enter 'h' or 's' ")
            if ask.lower() == 'h':
                hit(deck,hand)
            elif ask.lower() == 's':
                print("Player stands. Dealer is playing.")
                playing = False
            else:
                print("Sorry, please try again.")
                continue
            break
        
    def show_some(player,dealer):
        print("\nDealer's hand: ")
        print(" <card hidden> ")
        print('', dealer.cards[1])
        print('\nPlayers hand: ', player.cards[0],player.cards[1], sep='\n ')

    def show_all(player,dealer):
        print("\nDealer's hand: ", *dealer.cards, sep='\n ')
        print("Dealer's hand =", dealer.value)
        print("\nPlayer's hand:", *player.cards, sep='\n ')
        print("Player's hand =", player.value)
    
    def player_busts(player,dealer,chips):
        print("Player Busts!")
        chips.lose_bet()

    def player_wins(player,dealer,chips):
        print("Player wins!")
        chips.win_bet()

    def dealer_busts(player,dealer,chips):
        print("Dealer busts!")
        chips.win_bet()

    def dealer_wins(player,dealer,chips):
        print("Dealer wins!")
        chips.lose_bet()

    def push(player,dealer):
        print("Dealer and Player tie! Its a push.")