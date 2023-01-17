from os import system

bid_list = []
highest = 0

end = False
while not end:
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ")
  bid = float(input("What's your bid?: $"))
  new ={}
  new["name"] = name
  new["bid"] = bid
  bid_list.append(new)
  
  option = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  if option == 'yes':
    system("clear")
  else:
    end = True
  
  for person in bid_list:
    value = person["bid"]
    if value > highest:
      highest_bid = value
      highest_bidder = person["name"]

print("The winner is {} with a bid of ${}".format(highest_bidder, highest_bid))
