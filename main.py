import random
#cards
cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

#changes the string card names to int values
def nameToNum(card):
    if card == 'Ace':
        card = 11
    if card == 'Jack':
        card = 10
    if card == 'Queen':
        card = 10
    if card == 'King':
        card = 10

    return card

#dealCard function will deal out the init cards for the round
#if given two Aces, the first Ace will be valued at 11 and the second Ace is 1
def dealCard():
    card1 = random.choice(cards)
    card1 = nameToNum(card1)

    card2 = random.choice(cards)
    card2 = nameToNum(card2)

    #function will return the hand as an array of 2 cards
    hand = [card1, card2]
    return hand

def hit():
    card = random.choice(cards)
    card = nameToNum(card)
    return card

#dealer rules
#16 or lower the dealer must hit, 17 or higher the dealer stands
#dealer is init with two cards, the first card will be revealed to the players after dealing is over
class Dealer:
    hand = dealCard()
    card1 = hand[0]
    card2 = hand[1]
    total = card1 + card2

    def printCard1(self, card1):
        print('Card 1: ' + str(card1))

    def printEndGame(self, card2, total):
        print('Card 2: ' + str(card2))
        print('Total: ' + str(total))

    def rules(self, total, hand):
        while total < 16:
            print('Dealer hit')
            hitCard = hit()
            hand.append(hitCard)
            total += hitCard
            print(hitCard)
            print(total)

class Player:
    hand = dealCard()
    card1 = hand[0]
    card2 = hand[1]
    total = card1 + card2

    def printHand(self, total, hand):
        print('Card 1: ' + str(hand[0]))
        print('Card 2: ' + str(hand[1]))
        print('Total: ' + str(total))

    def choice(self, total, hand):
        print('\nSelect option: ')
        print('1. Hit')
        print('2. Split')
        print('3. Double')
        print('4. Stand')

def main():
    print('Welcome to Python Blackjack')
    print('Select an option:')
    print('1. Start')
    print('2. Quit')
    choice = int(input())

    if(choice == 1):
        #dealer starts with cards dealt and shows first card
        dealer = Dealer()
        print('Dealer: ')
        dealer.printCard1(dealer.card1)
        #dealer.rules(dealer.total, dealer.hand)

        #player is init and shown both cards
        player = Player()
        print('\nPlayer: ')
        player.printHand(player.total, player.hand)
        player.choice(player.total, player.hand)

        #end game, dealer shows second card and hits till >16
        print('\nEnd game: ')
        dealer.printEndGame(dealer.card2, dealer.total)
        dealer.rules(dealer.total, dealer.hand)
    else:
        print('Goodbye')

if __name__ == "__main__":
    main()
