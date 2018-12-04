#to check whether the player is using our cards, maybe we can give them all the
#string they need and dont let them declare string in input. So we can easily check
#if " or ' present in input then hitPlayer

#Some cards we can do:
"""
cards = ["immutable", "ability", "hello", " "]

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
plan to include tuples aswell for more variety
or can pre-assign something to a
cards = [("car","otter"),"fish",["avocado"]]
req: ["fish",("car", "otter"), "elements"]
solution: 
    cards.pop()
^this isn't done


i think we can leave most of this part for everyone else to do, this hurts my brain

we should make some rules for how we make the requirement
ex:
    [] if there are things in a list, ur supposed to move items in them around, could pre-assign
        a list to a, then solution is just a.pop(), a.insert(), ...

    "" if theres a string, supposed to slice[:] or loop to get chars, ...

    () if tuple, it can be a block inside a ["A", (123,21), "b"], so if solution requires looping
        there must be a clause for the tuple
        or cards = "123", "21", req: ["some",(123,21),"other stuff"], so .append(()) a tuple

these are just examples, can be better
"""
'''
as for the game:

    I want to move some stuff around, right now the flow is from player.endturn to player
then bounces around different objects, it would be better if objects dont call other objects so often.
Maybe it all gets handled by a function, then depending on the return of that function we continue or end
the game
Basically in an object dont use anotherObject's.method() if possible.

    while True to get multi line user input code can also be in a function, along with ur anti-cheat idea.

    Spells i plan to use a list of dictionaries [{}, {}, {}]
and possibly move all the damage taking logic into the spells, right now we have to call player.hit(damage)
and spell.atk1, it might be simpler to just call spell.spellName anytime we need to hit something,
so detected "" in code, spell.playerIsCheating; compile error, spell.playerCantFuckingCode;
spell not found in [{}], spell.playerAttempted.

pick anything from this ^ list.

i already learned a lot of turtle, so i can just teach u guys when im mostly done, still changing a lot
of stuff

and if u find or make anything that could be a player/boss model or background image put it up, if we have
time we can have player choose which model, or change boss model depending on stage.
'''

"""
cards = [["one", "two", "three", "four"], "five", "six", "seven", "eight", "nine", "ty"]

requirement: a list containing the first 4 prime numbers

requirement: "onetwotwothreethreethreefourfourfourfour"

requirement: ["eightynine", "seventynine"]

requirement: "onetwothreefour"
"""
