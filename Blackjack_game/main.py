############### Blackjack Project #####################
import random
from art import dic_arts
from replit import clear
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
user_cards = []
dealer_cards = []
key_result = 0
want_to_play = True
#print all cards
def print_cards(u_cards,d_cards):
    print(f"\tyour cards: {u_cards} score {calculate_score(u_cards)}")
    print(f"\tdealer cards: {d_cards} score {calculate_score(d_cards)}")
#deal a card if asked    
def dealer_hit():
    cards_len = len(cards)
    card_drawn = random.randint(0,cards_len-1)
    return cards[card_drawn]
#calculate score and retrun 0 if balackJack and decide value of A ika as 1 or 11
def calculate_score(cards_list):
    cards_sum = sum(cards_list)
    if cards_sum == 21:
        return 0
    elif 11 in cards_list:
        if cards_sum > 21:
            cards_sum  -= 10
        return cards_sum
    else:
        return cards_sum
        
start_game  = input("Do you want to play blackjack game 'y' or 'n'! : ")

if start_game == 'n':
    want_to_play = False

while want_to_play:
    print(dic_arts[9])
    for i in range(0,2):
        user_cards.append(dealer_hit())
        dealer_cards.append(dealer_hit())
    
    print(f"\tyour cards: {user_cards} score: {calculate_score(user_cards)}")
    print(f"\tdealer first card: {dealer_cards[0]}")

    #if sum of user cards is 21 and dealer card is not 21
    if calculate_score(user_cards) == 0 and calculate_score(dealer_cards) != 0:
        key_result = 0
    
    if calculate_score(user_cards) > 21:
        key_result = 1      
    
    while calculate_score(user_cards) < 21 and (key_result != 0 or key_result != 1):
        option = input("do you want to get another card 'y' or 'n' : ")
        if option == 'y':
            user_cards.append(dealer_hit())
            if calculate_score(user_cards) > 21:
                key_result = 1
                break
            if calculate_score(user_cards) == 0:
                key_result = 0
                break
            print(f"your cards {user_cards} score {calculate_score(user_cards)}")
            print(f"dealer cards {dealer_cards[0]}")
        else:
            while calculate_score(dealer_cards) < 17:
                dealer_cards.append(dealer_hit())
            if calculate_score(dealer_cards) == 0:
                key_result = 1
                break
            elif calculate_score(dealer_cards) > 21:
                pkey_result = 0
                print(dealer_cards)
                break
            else:
                if calculate_score(user_cards) > calculate_score(dealer_cards):
                    key_result = 0
                    break
                elif calculate_score(user_cards) < calculate_score(dealer_cards):
                    key_result = 1
                    break
                else:
                    key_result = 2
                    break
    print_cards(user_cards,dealer_cards)
    print(f"{dic_arts[key_result]}.")
    start_game  = input("Do you want to play blackjack game 'y' or 'n'! : ")
    if start_game == "n":
        want_to_play = False
    else:
        clear()
    
    user_cards.clear()
    dealer_cards.clear()

print("\nPlease come again to play blackjack")