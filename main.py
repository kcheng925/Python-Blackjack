import random
#cards
cards = ['Ace', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

#dealCard function will deal out the init cards for the round
#if given two Aces, the first Ace will be valued at 11 and the second Ace is 1
def dealCard():
    card1 = random.choice(cards)
    #card1 = 'Ace'
    #print('card 1 value:' + str(card1))
    #change the value of the strings to ints
    if card1 == 'Ace':
        card1 = 11
    if card1 == 'Jack':
        card1 = 10
    if card1 == 'Queen':
        card1 = 10
    if card1 == 'King':
        card1 = 10

    card2 = random.choice(cards)
    #card2 = 'Ace'
    #print('card 2 value: ' + str(card2))
    #change the value of the strings to ints
    if card2 == 'Ace' and card1 == 11:
        card2 = 1
    elif card2 == 'Ace':
        card2 = 11
    if card2 == 'Jack':
        card2 = 10
    if card2 == 'Queen':
        card2 = 10
    if card2 == 'King':
        card2 = 10

    total = card1 + card2
    #print('Dealer Total: ' + str(total))
    return total