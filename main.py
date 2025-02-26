import art
print(art.logo)

def find_max_bidder(bid):
    # TODO-4: Compare bids in dictionary
    winner_bid_amount = 0.0
    winner_bid_name = ""
    for name in bid:
        if bid[name] > winner_bid_amount:
            winner_bid_name = name
            winner_bid_amount = bid[name]

    print(f"\nThe winner, {winner_bid_name}, won with a bid of ${winner_bid_amount}. Congratulations!")

bid = {}
repeat = True

while repeat:
    # TODO-1: Ask the user for input
    name = input("What is your name?: ")
    bid_amount = float(input("How much are you bidding?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bid[name] = bid_amount
    # TODO-3: Whether if new bids need to be added
    repeat_response = input("Is there another bidder?('yes' or 'no'): ")
    if repeat_response == "no":
        repeat = False
        find_max_bidder(bid)
    else:
        print("\n" * 20)


