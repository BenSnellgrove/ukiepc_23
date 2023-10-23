# needs more fast

input_split = input().split()
piers = int(input_split[0])
cards = int(input_split[1])
events = int(input_split[2])

trips = {}
costs = {}

for card in range(1, cards + 1):
    costs[card] = 0

for i in range(events):
    input_split = input().split()
    pier = int(input_split[0])
    card = int(input_split[1])

    if not card in trips:
        trips[card] = pier
    else:
        start_pier = trips[card]
        if start_pier != pier:
            costs[card] += max(pier - start_pier, start_pier - pier) #i forgor how to abs in pythob
        else:
            costs[card] += 100

        del trips[card]

for card in trips: #leftover
    costs[card] += 100

for card in range(1, cards + 1):
    if card != cards:
        print(str(costs[card]), end=" ")
    else:
        print(str(costs[card]), end="")