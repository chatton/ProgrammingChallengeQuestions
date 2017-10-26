"""
Write a function turn_into_coins that will take
an amount of cash as an integer and return a map
of value -> no. of coins. Your function should return
the minimum requred coins and their denominations needed
to break up that amount of cash into change.
"""


num_coins = [1,2,5,10,20,50,100,200]

def turn_into_coins(total_cash):
    """Function returns back the number of each denomination in coins
    that make up the total_cash value."""
    if total_cash < 0:
        raise ValueError("Must provide a positive number of cash.")

    values = {}
    denominations = sorted(num_coins, reverse=True) # biggest values first.
    for num in denominations: # looking at every denomination of coin.
        while num <= total_cash: # look at this denomination until it's too big
            total_cash -= num # taking this amount away from the total cash
            val = values.get(num, 0) # start at 0 if we haven't had any of this type yet
            val += 1 # we now have one more
            values[num] = val
    return values


print(turn_into_coins(76)) # {50: 1, 20: 1, 5: 1, 1: 1}
print(turn_into_coins(2222)) # {200: 11, 20: 1, 2: 1}
print(turn_into_coins(0)) # {}
print(turn_into_coins(623)) # {200: 3, 20: 1, 2: 1, 1: 1}
print(turn_into_coins(12)) # {10: 1, 2: 1}
