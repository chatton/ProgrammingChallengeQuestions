def pair_sum(numbers, target_sum):

    seen = set()
    result = set()

    for num in numbers:
        # calculate the number that we need to reach the target sum 
        target = target_sum - num
        
        # if it's the first time seeing it, keep track
        if target not in seen:
            seen.add(num)
        else: # otherwise we've seen this number already and it will add up to target_Sum
            result.add( (min(num,target), max(num, target)))

    return result

assert len(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10)) == 6
assert len(pair_sum([1,2,3,1], 3)) == 1
assert len(pair_sum([1,3,2,2], 4)) == 2