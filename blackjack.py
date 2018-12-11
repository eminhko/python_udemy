
import random

suits = ('Hearts','Diamonds','Spades','Clubs')

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,
         'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True



class Card:
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        
        return f"{self.rank} of {self.suit}"


class Deck:
    
    def __init__(self):
        
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        s_card = self.deck.pop()
        return s_card
    
    #To check all cards in a deck
    #def __str__(self):
    #    tot_card = ''
    #    for item in self.deck:
    #        tot_card += '\n' + item.__str__()
    #    return tot_card


#If there is Ace in hand and value is greater than 21, count as 1 instead of 11
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value =0
        self.aces =0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
         
   
class Chips:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet 
    
    def lose_bet(self):
        self.total -= self.bet



def take_bet(chip):
    
    while True:
        try:
            chip.bet = int(input('How much bet would you like to bet?=  '))
        except ValueError:
            print('Please enter an integer')
        else:
            if chip.bet > Chips.total:
                print('You do not have enought chips')
            else:
                break
         

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input('Hit or stand?. Enter hit or stand: ')
        
        if x == 'hit':
            hit(deck,hand)
        elif x == 'stand':
            print('Player stands. Dealer is playing')
            playing = False
            
        else:
            print('Please enter hit or stand')
            continue
        break


def show_some(player,dealer):
    
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
   
