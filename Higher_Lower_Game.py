import random
from art import logo, vs
from game_data import data

#Todo
#1-compare A and B done
#2- checking cond
#               if false, give game score, exit
#               if true,
#               than iterate through loop and ask again,
#                    if correct than +1 score, if wrong give previous score and exit

#loop through list and dic value for Compare A
def options(n):
    compare_a_name=data[n]["name"]
    compare_a_description=data[n]["description"]
    compare_a_country=data[n]["country"]
    return f"{compare_a_name}, a {compare_a_description}, from {compare_a_country}" #Here if u use print than u would get stuck!

#Compare function handling comparision and game score
def compare(n1, n2, u_choice):
    if u_choice == 'a':
        if data[n1]["follower_count"] > data[n2]["follower_count"]:
             print(f"You are right! Current score: {game_score+1}")
             return True
        else:
             print(f"Sorry wrong guess. Your score is {game_score}, try again!")
             return False
             #exit()
    else:
        if data[n2]["follower_count"] > data[n1]["follower_count"]:
             print(f"You are right! Current score: {game_score+1}")
             return True
        else:
             print(f"Sorry wrong guess. Your score is {game_score}, try again!")
             return False
             #exit()

#Game begins
#Random generated n each time
#n1=random.randint(0,len(data)-1)
n2=random.randint(0,len(data)-1)
#if they both are same
#if n1 == n2:
#   n2 = random.randint(0, len(data))

continue_game=True
game_score=0
while continue_game:
    print(logo)
    n1 = n2                                      #Here you only need to generate n2 once no need for n1
    n2 = random.randint(0, len(data))
    if n1 == n2:
        n2 = random.randint(0, len(data))
    print(f"Compare A: {options(n1)}")
    print(vs)
    print(f"Against B: {options(n2)}")
    user_choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    continue_game=compare(n1,n2, user_choice)    #Here the calling and returning is handled in one line!
    game_score += 1


























