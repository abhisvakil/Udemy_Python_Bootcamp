import art
import random

#To generate random number in 1 to 100
def get_a_num():
    return random.choice(range(0,101))

#Global variable storing the answer should not be changed
ANSWER = get_a_num()

#To compare user choice each time with the answer
def compare(u_response):
        if u_response == ANSWER:
            print(f"You got it! The answer was {ANSWER}")
            exit()
        elif u_response > ANSWER:
            print("Too high.")
            print("Guess again.")
        elif u_response < ANSWER:
            print("Too low.")
            print("Guess again.")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_choice=input("Choose a difficulty. Type 'easy' or 'hard':").lower()

#Routing Logic based on difficulty
if difficulty_choice == 'easy':
    #10 Attempts for easy mode
    attempt = 10
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_response = int(input("Make a guess:"))
        compare(user_response)
        attempt -= 1
    print("You ran out of attempts, Please refresh again!")
else:
    attempt = 5
    while attempt > 0:
        print(f"You have {attempt} attempts remaining to guess the number.")
        user_response = int(input("Make a guess:"))
        compare(user_response)
        attempt -= 1
    print("You ran out of attempts, Please refresh again!")

