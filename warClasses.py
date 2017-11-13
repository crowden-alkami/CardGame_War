

import random



class Card():
	def __init__(self, suit, val):
		self.suit = suit
		self.val  = val

	def show(self):
		print("{} of {}".format(self.val, self.suit))

#Builds a deck of cards
class Deck():
	def __init__(self):
		self.cards = []
		self.build()

	#Build function that gets passed to the Card class and populates the self.cards list
	def build(self):
		for cardsuit in ["Diamonds", "Spades", "Hearts", "Clubs"]:
			for cardvalue in range(1, 14): 
				self.cards.append(Card(cardsuit, cardvalue))

	def show(self):
		for c in self.cards:
			c.show()

    #Shuffles the deck
	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0 , i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]	

	#Splits the deck into even halves for 2 players
	def deal(self):
		for i in self.cards:
			self.firstHalf = self.cards[:26]
			self.secondHalf = self.cards[26:]

	#Verifies that the deck has been dealt correctly.
	def showHands(self):
		for i in self.firstHalf:
		  i.show()
		for i in self.secondHalf:
		  i.show()
			

class Player():
	def __init__(self, name):
		self.name = name
		self.hand = []
 

	def playerHand(self):
	  x = 0
	  while(x < 26):
		  self.hand.append(deck.cards.pop())
		  x += 1
		  
	def show(self):
	  for i in self.hand:
	    i.show()


deck = Deck()
deck.shuffle()
deck.deal()
