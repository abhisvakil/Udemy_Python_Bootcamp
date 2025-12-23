from art import logo
import random

def deal_card():
    """Returns a random card from the list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choices(cards, k=2)
    return card

#here we have to take care of the ace being counted as 11 and
#1 depending on what is the sum of the 2 cards of either the user or computer
def calculate_score(cards):
    """Returns score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #if they go over 21 than ACE has to be counted as 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, Opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win!"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"



#Giving 2 random cards to user and computer
def play_game():
    print(logo)
    user_cards=deal_card()
    computer_cards=deal_card()
    computer_score= -1 #To remove the error from line 47th while Loop so that the even if computer score is not defined anywhere the code does not crash
    user_score = -1 #Same logic  as computer_score
    is_game_over=False

    #Keep all functions at the top so that u can all them later, like function cant be called before its declaration
    #while loop to continue the function till game is not over
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        #Condition if user or computer score is greater than 21 than game ends
        if user_score == 0 and computer_score == 0 or user_score > 21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, 'n' to pass")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    #Dealing logic for computer
    #!= 0 condition for blackjack
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    #All print statements required at the end!
    print(f"Your final hand: {user_cards}, final_score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Continueing the game logic
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    print("\n" * 200)
    play_game()

