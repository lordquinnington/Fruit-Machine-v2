## fruit machine II

import random, time

numberOfReels = int(input("enter a number of reels >"))    # asks the user how many reels they would like to play with
symbols = ['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']    # initial array of symbols
print("symbols array:", symbols)
addSymbol = input("type a fruit to add to the symbols, or press enter to skip >")    # asks the user if they want to play with any more symbols
while addSymbol != "":
    symbols.append(addSymbol)    # adds a symbol to the array if the user does want to play with more
    print("new symbols array:", symbols)
    addSymbol = input("type another fruit to add to the symbols, or press enter to skip >")
winnings = 1.00    # gives the user a starting amount of £1

def countRepeats(itemsRolled, toCheck):    # function to count the number of symbols repeated, to allow for a varied number of reels, with thanks to Oliver
    count = 0
    for x in range(len(itemsRolled)):
        if itemsRolled[x] == toCheck:
            count += 1    # adds 1 to a counter for each time a symbol is repeated
    return count    # return the number of times the symbol being checked appears in the array of rolls

def winningsCalc(itemsRolled, winnings):    # function to calculate how much the user has won
    for x in range((len(itemsRolled)-1)):
        numberOfRepeats = countRepeats(itemsRolled, itemsRolled[x])
        if numberOfRepeats >= (len(itemsRolled) - 1):    # if the symbol appears almost all the time, it is classed as a repeated symbol
            repeatedSymbol = itemsRolled[x]
            break
    if numberOfRepeats == numberOfReels:    # if all the symbols are the same
        if repeatedSymbol == 'Skull':
            return 0    # the user loses all their money if they get all skulls
        elif repeatedSymbol == 'Bell':
            return winnings + 5.00    # the user gets £5 if all the symbols are bells
        else:
            return winnings + 1.00    # the user gets £1 if all the symbols are the same
    elif numberOfRepeats == (numberOfReels - 1):    # if almost all but one of the symbols are the same
        if repeatedSymbol == 'Skull':
            return winnings - 1.00    # the user loses £1 if all but one are skulls
        else:
            return winnings + 0.50    # the user gets 50p for any other symbols
    else:
        return winnings    # the user gets nothing extra if not enough of the symbols match

def spinFruitMachine():    # function to spin the fruit machine
    itemsArray = []    # array to store the symbols rolled
    for x in range(numberOfReels):
        itemsArray.append(random.choice(symbols))    # appends a random symbol onto the array
    return itemsArray

def playFruitMachine(winnings):    # function to play the fruit machine
    itemsRolled = spinFruitMachine()    # gets the array of symbols rolled
    winnings = round((winningsCalc(itemsRolled, winnings) - 0.20), 2)    # calculates the winnings for the user (subtracting the playing fee) and rounds
    return winnings, itemsRolled

play = input("to roll (20p), press enter, to quit with winnings, press any other key >")    # asks the user if they want to play the fruit machine
while play == "":
    winnings, itemsRolled = playFruitMachine(winnings)
    for x in range(numberOfReels):    # loop to print the symbols rolled to the user
        print(itemsRolled[x])
        time.sleep(0.7)
    print("you have £"+ str(winnings) +"0")    # outputs the users current winnings
    if winnings >= 0.20:    # if the user has more than 20p, they are allowed to play again
        play = input("press enter to roll again (20p), press any other key to quit with your winnings >")
    else:    # if the user can't afford to play again, the game quits
        break
print("you have won £"+ str(winnings) +"0. Byeee")    # outputs the user's final winnings to them   
