import random
import time

#Create a deck of cards, 0-Card in deck, 1-Card on hard, 2-Card used or discarded
def createDeck(deck):
	for i in range(8):
		deck.append(0)

#Distribute 4 cards to cardOnHand from deck, to used at the beginning of the game
def distribute4Cards(cardsOnHand, deck):
	for i in range(4):
		distributeCard(cardsOnHand, deck)

#Distribute one card to cardOnHand from deck and set deck[ran] = 1
def distributeCard(cardsOnHand, deck):
	ran = random.randint(0, 7)
	while deck[ran] != 0:
		ran = random.randint(0, 7)
	cardsOnHand.append(ran)
	deck[ran] = 1

#Print cards that user has on hand
def printCard(user):
	print("These are your cards:")
	if 0 in user:
		print("Card 0: s.split('f')")
	if 1 in user:
		print("Card 1: s.split('i')")
	if 2 in user:
		print("Card 2: s[10] = 'd'")
	if 3 in user:
		print("Card 3: s[1] = 'e'")
	if 4 in user:
		print("Card 4: s = s[:10]")
	if 5 in user:
		print("Card 5: s = 'e'.join(s)")
	if 6 in user:
		print("Card 6: s = 'd'.join(s)")
	if 7 in user:
		print("Card 7: s = s + 'd'")


#Tell user its his/her turn
def printUserTurn(user, s, l):
	print("Now is your turn, you can use or discard one of your cards each turn and I will distribute you one new card.\n")	
	printCard(user)
	print("\nThe current string and list are...\ns = ", s, "\nl = ", l, "\n")


#Discard card from cardsOnHand, adjust deck[i] to 2
def discardCard(cardsOnHand, deck, card):
	cardsOnHand.remove(card)
	deck[card] = 2
	print("You discarded card", card)

#Use card i, adjust deck[i]
def useCardString(cardsOnHand, deck, card, s):
	if card == 0:
		if isinstance(s, list):
			print("AttributeError: 'list' object has no attribute 'split'")
		else:
			s = s.split('f')
			print("s = s.split('f')")

	elif card == 1:
		if isinstance(s, list):
			print("AttributeError: 'list' object has no attribute 'split'")
		else:
			s = s.split('i')
			print("s = s.split('i')")

	elif card == 2: #s[10] = 'd'
		if isinstance(s, list):
			print("TypeError: 'str' object does not support item assignment")
		else:
			print("IndexError: list assignment index out of range")

	elif card == 3:
		if isinstance(s, list) and len(s) >= 2:
			s[1] = 'e'
			print("s[1] = 'e'")
		else:
			print("TypeError: 'str' object does not support item assignment")

	elif card == 4:
		s = s[:10]
		print("s = s[:10]")

	elif card == 5:
		s = 'e'.join(s)
		print("s = 'e'.join(s)")

	elif card == 6:
		s = 'd'.join(s)
		print("s = 'd'.join(s)")

	elif card == 7:
		if isinstance(s, list):
			print('TypeError: can only concatenate list (not "str") to list')
		else:
			s = s + 'd'
			print("s = s + 'd'")

	cardsOnHand.remove(card)
	deck[card] = 2
	return s

#User's move
def userMove(cardsOnHand, deck, s):
	i = input("What's your move? (eg. Use 1 or Discard 4)\n")
	i = i.split(" ")
	while len(i) != 2:
		print("Try again...")
		return userMove(cardsOnHand, deck, s)
	card = int(i[1])
	while i[0].lower() != "discard" and i[0].lower() != "use":
		print (i[0])
		print("Do you want to use a card or discard a card? Try again...")
		return userMove(cardsOnHand, deck, s)
	while deck[card] != 1:
		print("You don't have that card, try again.")
		return userMove(cardsOnHand, deck, s)
	if i[0].lower() == "discard":
		discardCard(cardsOnHand, deck, card)
	if i[0].lower() == "use":
		s = useCardString(cardsOnHand, deck, card, s)
	print("The string is now: s = ", s, "\n\n")
	return s

#Comp's move
def compMove(cardsOnHand, deck, l):
	print("Now is your opponent's turn...\n")
	time.sleep(1)
	card = 0
	if 0 in cardsOnHand:
		l[4] = 11
		print("Your opponent used Card ", card, "\nResult: ls[4] = 11")
	elif 1 in cardsOnHand:
		l[5] = 13
		card = 1
		print("Your opponent used Card ", card, "\nResult: ls[5] = 13")
	else: #no useful card
		card = cardsOnHand[0]
		print("Your opponent discarded Card ", card)
	cardsOnHand.remove(card)
	deck[card] = 2
	print("l is now: ", l, "\n\n")
	return l





print('\nI have an incorrect list of the first 6 prime numbers and a string with spelling errors:\ns = "Hillo worlf"\nl = [2, 3, 5, 7, 13, 17]\n\nCan you and your opponent choose one each and help me to fix it? (Please enter "Yes" or "No"')

i = input().lower()
while i != "yes" and i != "no":
	i = input('Please enter "Yes" or "No"\n').lower()
if i == "no":
	import sys
	sys.exit("Bye")

print("\nGreat, I will distribute you and your opponent 4 cards each. Each card contains a line of code to modify the string or list. The one who correct the string or list first wins! Distributing cards...\n")
time.sleep(2)

#Create 2 decks of cards
deckString = []
deckList = []
createDeck(deckString)
createDeck(deckList)

#Distribute cards to user and comp
user = []
comp = []
distribute4Cards(user, deckString)
distribute4Cards(comp, deckList)

s = "Hillo worlf"
l = [2, 3, 5, 7, 13, 17]

count = 4
while s != "Hello world" and l != [2, 3, 5, 7, 11, 13]:
	printUserTurn(user, s, l)

	s = userMove(user, deckString, s)

	l = compMove(comp, deckList, l)

	if count == 8:
		print("There's no card left in the deck.")
	else:
		distributeCard(user, deckString)
		distributeCard(comp, deckList)
		count += 1

if s == "Hello world":
	print("You win!! C:")

elif l == [2, 3, 5, 7, 11, 13]:
	print("You lose :C")


"""
l = [2, 3, 5, 7, 13, 17]
0l[4] = 11
1l[5] = 13

2l[3] = 6???
3l = ' '.join(l)???
4l = l.split("13")???
5l = '11'.join(l)???
6l = l.split("17")???
7l = l + '13'
"""
