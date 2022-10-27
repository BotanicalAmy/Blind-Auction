from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidder is the key in the dictionary, bid_amount is the value
    #bidder matches to the name(key) in the bid dictionary, and the bid_amount matches the price (value) in the bid dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        #checking each bid as it's entered, replacing the highest bid record if the newly entered bid is higher
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What's your bid? $"))
    #defining that the name is the key in the empty bid list, and the price is the value
    bids[name] = price
    should_continue = input("Are there any other bidders?  Type 'yes' or 'no'")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()