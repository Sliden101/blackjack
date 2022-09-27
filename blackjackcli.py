import random
dealerValue = 0
playerValue = 0
deck = ['A♥','A♦','A♠','A♣','2♥','2♦','2♣','2♠','3♥','3♦','3♣','3♠','4♥','4♦','4♣','4♠','5♥','5♦','5♣','5♠','6♥','6♦','6♣','6♠','7♥','7♦','7♣','7♠','8♥','8♦','8♣','8♠','9♥','9♦','9♣','9♠','10♥','10♦','10♣','10♠','J♥','J♦','J♠','J♣','Q♥','Q♦','Q♠','Q♣','K♥','K♦','K♠','K♣']
deckDict = {'A♥':1,'A♦':1,'A♠':1,'A♣':1,'2♥':2,'2♦':2,'2♣':2,'2♠':2,'3♥':3,'3♦':3,'3♣':3,'3♠':3,'4♥':4,'4♦':4,'4♣':4,'4♠':4,'5♥':5,'5♦':5,'5♣':5,'5♠':5,'6♥':6,'6♦':6,'6♣':6,'6♠':6,'7♥':7,'7♦':7,'7♣':7,'7♠':7,'8♥':8,'8♦':8,'8♣':8,'8♠':8,'9♥':9,'9♦':9,'9♣':9,'9♠':9,'10♥':10,'10♦':10,'10♣':10,'10♠':10,'J♥':10,'J♦':10,'J♠':10,'J♣':10,'Q♥':10,'Q♦':10,'Q♠':10,'Q♣':10,'K♥':10,'K♦':10,'K♠':10,'K♣':10}
deckVal = list(map(deckDict.get, deck))
dealerCard1 = random.choice(deck)
dealerIndex1 = deck.index(dealerCard1)
dealerValue += deckVal[dealerIndex1]
deck.remove(dealerCard1)
dealerCard2 = random.choice(deck)
dealerIndex2 = deck.index(dealerCard2)
dealerValue += deckVal[dealerIndex2]
deck.remove(dealerCard2)
dealerHand = [dealerCard1, dealerCard2]
playerCard1 = random.choice(deck)
playerIndex1 = deck.index(playerCard1)
playerValue += deckVal[playerIndex1]
deck.remove(playerCard1)
playerCard2 = random.choice(deck)
playerIndex2 = deck.index(playerCard2)
playerValue += deckVal[playerIndex2]
deck.remove(playerCard2)
playerHand = [playerCard1, playerCard2]
print('Welcome to Blackjack!')
print('Rules: You play against the dealer.\nYou start with two cards.\n You can hit as many times as you want.\n If you go over 21, you lose.\n If you get 21, you win.\n If you get a higher value than the dealer without going over 21, you win.\n If you get a lower value than the dealer without going over 21, you lose.\n If you get the same value as the dealer, you lose.\n')
print("Your hand: " + str(playerHand))
choice = str(input('Hit or stand? '))
choice.lower()
def stand():
    global playerValue
    global playerHand
    global dealerValue
    global dealerHand
    global deck
    global deckVal
    if dealerValue <= 16:
        dealerCard = random.choice(deck)
        dealerIndex = deck.index(dealerCard)
        dealerValue += deckVal[dealerIndex]
        deck.remove(dealerCard)
        dealerHand.append(dealerCard)
    print('Dealer hand: ' + str(dealerHand))
    if dealerValue > 21:
        print('You win!')
    if playerValue < dealerValue:
        print("You lose!")
    if playerValue > dealerValue:
        print('You win!')
def hit():
    global playerValue
    global playerHand
    global deck
    global deckVal
    playerCard = random.choice(deck)
    playerIndex = deck.index(playerCard)
    playerValue += deckVal[playerIndex]
    deck.remove(playerCard)
    playerHand.append(playerCard)
    print("Your hand: " + str(playerHand))
    if playerValue == 21:
        print('You win!')
        quit()
    if playerValue > 21:
        print("You lose!")
        quit()
    choice = str(input('Hit or stand? '))
    choice.lower()
    if choice == 'hit':
        hit()
    else:
        stand()
if choice == 'hit':
    hit()
else:
    stand()
