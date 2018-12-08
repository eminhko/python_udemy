
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
    
    def __str__(self):
        tot_card = ''
        for item in self.deck:
            tot_card += '\n' + item.__str__()
        return tot_card
