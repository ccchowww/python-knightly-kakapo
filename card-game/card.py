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
	print("Now is your turn, you can use or discard one of your cards each turn and I will distribute you one new card on the next round.\n")	
	printCard(user)
	print("\nThe current string and list are...\ns = ", s, "\nl = ", l, "\n")


#Discard card from cardsOnHand, adjust deck[i] to 2
def discardCard(cardsOnHand, deck, card):
	cardsOnHand.remove(card)
	deck[card] = 2
	print("You discarded card", card)
	time.sleep(1)

#Use card i, adjust deck[i]
def useCardString(cardsOnHand, deck, card, s):
	time.sleep(1)
	if card == 0:
		if isinstance(s, list):
			print("AttributeError: 'list' object has no attribute 'split'")
			print("Oh no, that is an invalid move!")
			print("Reason: The split() function splits the original string and return a list of seperated strings. It can only be called on a string.")
			time.sleep(5)
		else:
			s = s.split('f')
			print("Result: s = s.split('f')")
			time.sleep(1)

	elif card == 1:
		if isinstance(s, list):
			print("AttributeError: 'list' object has no attribute 'split'")
			print("Oh no, that is an invalid move!")
			print("Reason: The split() function splits the original string and return a list of seperated strings. It can only be called on a string.")
			time.sleep(5)
		else:
			s = s.split('i')
			print("Result: s = s.split('i')")
			time.sleep(1)

	elif card == 2: #s[10] = 'd'
		if isinstance(s, list):
			print("TypeError: 'str' object does not support item assignment")
			print("Oh no, that is an invalid move!")
			print("Reason: String is an immutable object in Python, so its character cannot be modified once created.")
			time.sleep(5)
		else:
			print("IndexError: list assignment index out of range")
			print("Oh no, that is an invalid move!")
			print("Reason: The position does not exist in the list, you cannot access an index value that exceeds the length of your list.")
			time.sleep(5)

	elif card == 3:
		if isinstance(s, list) and len(s) >= 2:
			s[1] = 'e'
			print("Result: s[1] = 'e'")
			time.sleep(1)
		else:
			print("TypeError: 'str' object does not support item assignment")
			print("Oh no, that is an invalid move!")
			print("Reason: String is an immutable object in Python, so its character cannot be modified once created.")
			time.sleep(5)

	elif card == 4:
		s = s[:10]
		print("Result: s = s[:10]")

	elif card == 5:
		s = 'e'.join(s)
		print("Result: s = 'e'.join(s)")

	elif card == 6:
		s = 'd'.join(s)
		print("Result: s = 'd'.join(s)")

	elif card == 7:
		if isinstance(s, list):
			print('TypeError: can only concatenate list (not "str") to list')
			print("**EXPLAINATION**")
		else:
			s = s + 'd'
			print("Result: s = s + 'd'")

	cardsOnHand.remove(card)
	deck[card] = 2
	return s

#Check validity of user's move, not valid->ask again for input, valid->carry out the move
def userMove(cardsOnHand, deck, s):
	i = input("What's your move? (Use/Discard <Card no.> Eg. Use 3/Discard 2)\n")
	i = i.split(" ")
	print("")
	if len(i) != 2:
		print("Please ensure you enter your choice in a correct format, try again...")
		return userMove(cardsOnHand, deck, s)
	card = int(i[1])
	if i[0].lower() != "discard" and i[0].lower() != "use":
		print("Do you want to use a card or discard a card? Try again...")
		return userMove(cardsOnHand, deck, s)
	elif deck[card] != 1:
		print("You don't have that card, try again.")
		return userMove(cardsOnHand, deck, s)
	elif i[0].lower() == "discard":
		discardCard(cardsOnHand, deck, card)
	elif i[0].lower() == "use":
		s = useCardString(cardsOnHand, deck, card, s)
	print("The string is now: s = ", s, "\n\n")
	return s

#Comp's move
def compMove(cardsOnHand, deck, l):
	print("Now is your opponent's turn...\n")
	time.sleep(3)
	card = 0
	r = random.random()
	if r >0.1:
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
	else:
		card = cardOnHand[len(cardsOnHand) - 1]
		print("Your opponent discarded Card ", card)
	cardsOnHand.remove(card)
	deck[card] = 2
	print("l is now: ", l, "\n\n")
	time.sleep(2)
	return l

def newRound(round):
	print("===========ROUND ", round, "===========\n")


def game():

	print('\nI have an incorrect list of the first 6 prime numbers and a string with spelling errors:\ns = "Hillo worlf"\nl = [2, 3, 5, 7, 13, 17]\n\nCan you and your opponent choose one each and help me to fix it? (Please enter "Yes" or "No")')

	i = input().lower()
	while i != "yes" and i != "no": #while reply not valid
		i = input('Please enter "Yes" or "No"\n').lower() #ask for input again
	if i == "no": #if reply == no
		import sys 
		sys.exit("Bye") #stop the program

	print("\nGreat, I will distribute you and your AI controlled opponent 4 cards each. Each card contains a line of code to modify the string or list. The one who correct the string or list first wins! Distributing cards...\n")
	time.sleep(6) #delay the program

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

	#create string and list
	s = "Hillo worlf"
	l = [2, 3, 5, 7, 13, 17]

	round = 0 #to keep track of what round are we at

	while s != "Hello world" and l != [2, 3, 5, 7, 11, 13]: #game continues if both list and string havent been completed
	
		round += 1 #increment round
		newRound(round) #print new round

		printUserTurn(user, s, l) #Tell player it's his/her turn

		s = userMove(user, deckString, s) #Check validity of user's move, not valid->ask again for input, valid->carry out the move

		l = compMove(comp, deckList, l) #Comp carries out move

		if round > 4: #if no card left in deck
			print("There's no card left in the deck.\n") #stop distributing cards at the end of each round
		else:
			distributeCard(user, deckString) #distribute card to user at the end of each round
			distributeCard(comp, deckList) #distribute card to comp at the end of each round

	if s == "Hello world": #if string is successfully modified
		print("You win!! C:\n")
		return True

	elif l == [2, 3, 5, 7, 11, 13]: #if list is successfully modified
		print("You lose :C\nPlease restart the game.")
		time.sleep(2)
		return False

x = False
while not x:
	x = game()

print("..")
