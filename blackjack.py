import random;

deck=['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4
card_tally={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
i=0

# Distribute Card
def distribute_card(deck):
    return deck.pop(0)

# Calculate Turn
def calculate_total(hand):
    total=sum(card_tally[card] for card in hand)
    
    for card in hand:
        if card=="A" and total>21:
            total-=10

    return total

# Player's turn 
def player_turn(deck,hand):

    while True:
        player_choice=input("Enter hit or stand: ").lower() 
        match player_choice:
            case "hit":
                hand.append(distribute_card(deck))
                total=calculate_total(hand)
                print("Your hand: ",hand, "Total: ",total)
                if total>21:
                    print("Bust! You lost.")
                    return False
            case "stand":   
                return True 
            case _:
                print("Incorrect input ")
                continue

# Dealer's turn 
def dealer_turn(deck,hand):
        while calculate_total(hand)<15:
            hand.append(distribute_card(deck))
        
        return hand

# Main chunk 
def main(deck):
    random.shuffle(deck)
   
    # Distribute cards initially:
    player_hand=[distribute_card(deck),distribute_card(deck)]
    dealer_hand=[distribute_card(deck),distribute_card(deck)]

    print("Your hand: ",player_hand, "Your total: ",calculate_total(player_hand))
    print("Dealers hand: ",dealer_hand[0])

    # if player stands then enters this loop
    if player_turn(deck,player_hand):
        dealer_hand=dealer_turn(deck,dealer_hand)   

        # Game finished, dealer also stands
        dealer_total=calculate_total(dealer_hand)
        player_total=calculate_total(player_hand)

        print("Dealer's hand: ", dealer_hand, "Dealer's total: ",dealer_total)

        # Determining Winner
        if dealer_total>21 or dealer_total<player_total:
            print("You win !!!")
        elif dealer_total==player_total:
            print("Draw !!!")
        else:
            print("Dealer win !!")

    # Play again or not
    while True:
        play_again_input=input("Play Again (y/n): ").lower()

        match play_again_input:
            case "y":
                deck=['2','3','4','5','6','7','8','9','10','J','Q','K','A'] * 4
                main(deck)
                return
            case "n":
                print("Thank you for playing. Have a nice day !!!")
                return
            case _:
                print("Invalid input. Press either y or n ")
                continue
           

# Execute the program
numbers = [1, 2, 3, 4, 5]
even_square_dict = {x: x**2 for x in numbers if x % 2 == 0}
print(even_square_dict)  # Output: {2: 4, 4: 16}
main(deck)
