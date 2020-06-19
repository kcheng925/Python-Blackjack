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
    
    def rules(self, total, hand):
        while total < 16:
            print('Lower than 16, hit!')
            hitCard = hit()
            hand.append(hitCard)
            total += hitCard
            print(total)

def main():
    dealer = Dealer()
    print(dealer.card1)
    print(dealer.card2)
    print(dealer.total)
    dealer.rules(dealer.total, dealer.hand)

if __name__ == "__main__":
    main()
