#to check whether the player is using our cards, maybe we can give them all the
#string they need and dont let them declare string in input. So we can easily check
#if " or ' present in input then hitPlayer

#Some cards we can do:
"""
cards = [immutable", "ability", "hello", " "]

requirement: "mutability" 
a = cards[0][2:5] + cards[1]

requirement: ["m", "u", "t", "a", "b", "l", "e"] 
a = cards[0][2:].split()

requirement: "hello mutability"
a = cards[2] + cards[3] + cards[2:5] + cards[1]

requirement: "heloo"
a = cards[3][:3] + 2 * cards[3][4]

"""

"""
cards = [["one", "two", "three", "four"], "five", "six", "seven", "eight", "nine", "ty"]

requirement: a list containing the first 4 prime numbers

requirement: "onetwotwothreethreethreefourfourfourfour"

requirement: ["eightynine", "seventynine"]

requirement: "onetwothreefour"
"""
