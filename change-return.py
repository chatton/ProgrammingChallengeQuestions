
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
            total_cash -= num
            val = values.get(num, 0)
            val += 1
            values[num] = val
    return values


print(turn_into_coins(76))
print(turn_into_coins(2222))
print(turn_into_coins(0))
print(turn_into_coins(623))
print(turn_into_coins(12))
