#  File: Blackjack.py
#  Description: Simulates one round of Blackjack between two players, a person and the dealer
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/22/16
#  Date Last Modified:9/23/16

import random

class Card:
    def __init__(self, suit, pip):
        self.suit = suit
        self.pip = pip
        if pip == "A":
            self.value = 11
        if pip.isdigit():
            self.value = int(pip)
        if ((pip == "J") or (pip == "Q") or (pip == "K")):
            self.value = 10
            
    def __str__(self):
        return self.pip + self.suit

class Deck:
    def __init__(self):
        self.cardList = []
        suitList = ["C","D","H","S"]
        pipList = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for i in range(4):
            for j in range(13):
                newCard = Card(suitList[i],pipList[j])
                self.cardList.append(newCard)
                
    def shuffle(self):
        random.shuffle(self.cardList)
        
    def dealOne(self,player):
        card = self.cardList.pop(0)
        player.hand.append(card)
        player.handTotal += card.value

    def __str__(self):
        count = 0
        i = 0
        while i < len(self.cardList):
            if count == 13:
                print("")
                count = 0
            print(self.cardList[i], end = " ")
            count += 1
            i += 1
        return ""

class Player:
    def __init__(self):
        self.hand = []
        self.handTotal = 0

    def __str__(self):
        handSize = len(self.hand)
        i = 0
        while i < handSize:
            print(self.hand[i], end = " ")
            i += 1
        return ""
        

def showHands(opponent,dealer):
    print("Dealer shows ", end = "")
    print(dealer.hand[1], end = "")
    print(" faceup")
    print("You show ", end = "")
    print(opponent.hand[1], end = "")
    print(" faceup") 
    


def opponentTurn(cardDeck,dealer,opponent):
    inPlay = True
    aceIs11 = False
    numAces = 0
    if ((opponent.hand[0].pip == "A") or (opponent.hand[1].pip == "A")):
        aceIs11 = True
        print("Assuming 11 points for an ace you were dealt for now.")
        numAces += 1
    print("You hold ", end = "")
    print(opponent, end = " ")
    print("for a total of " + str(opponent.handTotal))
    if opponent.handTotal == 21:
        print("21! My turn...")
        return
    while inPlay:
        userInput = input("1 (hit) or 2 (stay)?")
        if userInput == "1":
            cardDeck.dealOne(opponent)
            print("Card dealt: ", end = "")
            print(opponent.hand[-1])
            if opponent.hand[-1].pip == "A":
                aceIs11 = True
                numAces += 1
                print("Assuming 11 points for an ace you were dealt for now.")
                print("")
            if numAces > 1:
                print("Over 21. Switching aces from 11 to 1.")
                opponent.handTotal -= 10 * numAces
            if ((opponent.handTotal > 21) and (aceIs11)):
                aceIs11 = False
                print("Over 21. Switching an ace from 11 points to 1.")
                opponent.handTotal -= 10 * numAces
                print("New total: " + str(opponent.handTotal))
                numAces -= 1
            if opponent.handTotal > 21:
                print("Over 21. You lose.")
                return
            if opponent.handTotal == 21:
                print("21! My turn...")
                return
            print("You hold ", end = "")
            print(opponent, end = "")
            print(" for a total of " + str(opponent.handTotal))
        else:
            inPlay = False
            print("Staying with " + str(opponent.handTotal))
        print("")
            
            
def dealerTurn(cardDeck,dealer,opponent):
    if opponent.handTotal > 21:
        return
    inPlay = True
    aceIs11 = False
    numAces = 0
    print("Dealer's turn")
    print("Your hand: ", end = "")
    print(opponent, end = "")
    print(" for a total of " + str(opponent.handTotal))
    print("Dealer's hand: ", end = "")
    print(dealer, end = "")
    print(" for a total of " + str(dealer.handTotal))
    print("")
    if (dealer.handTotal >= opponent.handTotal):
        print("Dealer has " + str(dealer.handTotal) + ". Dealer wins!")
        return
    if ((dealer.hand[0].pip == "A") or (dealer.hand[1].pip == "A")):
        aceIs11 = True
        numAces += 1
        print("Assuming 11 points for an ace I was dealt for now")
        print("")
    while dealer.handTotal < opponent.handTotal:
        cardDeck.dealOne(dealer)                  
        print("Dealer hits: ", end = "")
        print(dealer.hand[-1])
        if dealer.hand[-1].pip == "A":
            aceIs11 = True
            numAces += 1
            print("Assuming 11 points for an ace you were dealt for now.")
        print("New total: " + str(dealer.handTotal))
        print("")
        if ((dealer.handTotal > 21) and (aceIs11)):
            aceIs11 = False
            print("Over 21. Switching an ace from 11 points to 1.")
            dealer.handTotal -= 10 * numAces
            print("New total: " + str(dealer.handTotal))
            print("")
        if dealer.handTotal > 21:
            print("Dealer has " + str(dealer.handTotal) + ". Dealer busts! You win.")
            return
        if (dealer.handTotal >= opponent.handTotal):
            print("Dealer has " + str(dealer.handTotal) + ". Dealer wins!")
            return

       


def main():

    cardDeck = Deck()
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    print("")
    
    #random.seed(25)                 # leave this in for grading purposes
    cardDeck.shuffle()
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see what resulted from your shuffle
    print("")
    
    dealer = Player()
    opponent = Player()
    
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face down
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face up


    print("Deck after dealing two cards each:")
    print(cardDeck)
    print("")

    
    showHands(opponent,dealer)      # remember not to show face down cards

    print("You go first.")
    print("")
    
    opponentTurn(cardDeck,dealer,opponent)
    print("")
    dealerTurn(cardDeck,dealer,opponent)
    print("")
    
    print ("Game over.")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   Opponent: ", opponent)
    


main()
        
