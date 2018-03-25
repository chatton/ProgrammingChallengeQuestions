def find_missing_element(l1, l2):
    num = 0
    for item in l1 + l2:
        num ^= item
    return num

print(find_missing_element([1,2,3,4,5], [1,3,4,5]))