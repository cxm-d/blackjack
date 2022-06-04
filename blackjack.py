import random
playerIn = True
dealerIn = True


#deck of cards / player - dealer hand
deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
playerHand = []
dealerHand = []


#deal cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


#calculate the total of each hand
def total(turn):
    total = 0 
    face = ['A','J','Q','K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

#check game state

def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

#loop back

for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

print(f'Dealer has {dealerHand}')
print(f'Player has {playerHand}')

while playerIn or dealerIn:
    print(f'Dealer has {revealDealerHand()} and a facedown card')
    print(f'You have {playerHand} for a total of {total(playerHand)}')
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn == False
    else:
        dealCard(playerHand)
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"/nYou have {playerHand} for a total of 21 and the dealer has {dealerHand} for a total of total({dealerHand})")
elif total(dealerHand) == 21:
    print(f"/nYou have {playerHand} for a total of 21 and the dealer has {dealerHand} for a total of total({dealerHand})")
elif total(playerHand) > 21:
    print(f"/nYou have {playerHand} for more than 21 and the dealer has {dealerHand} for a total of total({dealerHand})")
elif total(dealerHand) > 21:
    print(f"/nYou have {playerHand} and the dealer has {dealerHand} for a total of total({dealerHand})")
    print('Dealer bust and you win')
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"/nYou have {playerHand} and the dealer has {dealerHand} for a total of total({dealerHand})")
    print("Dealer wins")
elif 21 - total(playerHand) < 21 - total(dealerHand):
    print(f"/nYou have {playerHand} and the dealer has {dealerHand} for a total of total({dealerHand})")
    print("Player wins")