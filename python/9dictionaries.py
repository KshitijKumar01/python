# travel_log = [
#     {
#     "country" : "France",
#     "visits" : 12,
#     "cities" : ["paris", "lille", "Dijon"]
#     },
#     {
#     "country" : "Germany",
#     "visits" : 5,
#     "cities" : ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]

# for i in range(0, len(travel_log)):
#     for key in travel_log[i]:
#         print(travel_log[i][key])

# def add_new_log(country, vistis, lt):
#     d = {}
#     d["country"] = country
#     d["visits"] = vistis
#     d["cities"] = lt
#     travel_log.append(d)


# add_new_log("india", 3, ["lko", "agra", "amritsar"])

# for i in range(0, len(travel_log)):
#     for key in travel_log[i]:
#         print(travel_log[i][key])


from replit import clear

def find_heghest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        price = bids[bidder]
        if(price > highest_bid):
            highest_bid = price
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")


bids = {}
do = True  
while do :
    name = input("Enter your name : ")
    price = int(input("What is your bid : "))
    bids[name] = price 
    choice = input("Are there any more bidders type 'yes or 'no : ")
    if(choice == "no"):
        do = False
        find_heghest_bidder(bids)
    elif(choice == "yes"):
        clear()
    



