# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

# user_name = input("What is your name?\n").lower()
# user_bid = int(input("What's your bid?\n"))
# other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
auction={}
loop = True
while loop == True:
    user_name = input("What is your name?\n").lower()
    user_bid = int(input("What's your bid?\n"))
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    auction[user_name]=user_bid
    highest_bid=0
    for key in auction:
        if auction[key] > highest_bid:
            highest_bid = auction[key]
            winner = key
    if other == "yes":
        print("\n*100")
    if other == "no":
        loop = False
print(f"The winner is {winner}")


