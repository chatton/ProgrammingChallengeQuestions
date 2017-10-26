
"""Given an array of integers that represents towers and heights.
Write a function that returns True/False for if the array is jumpable.

A Jumpable array is one in which you can traverse in "jumps". A Tower of height 2
allows you jump 2 spaces. A Tower of height 1 allows you to jump 1 space.

You can only jump to the right.

You must be "outside" the array to have jumped over it.
Getting to the last index is not enough.

The array [3,0,2,0,1,1] is jumpable.
The array [3,0,2,0,1,0] is not jumpable.
The array [1,1,2,0,0,0] is not jumpable."""

arr = [3,0,2,0,1,1]
arr2 = [1,1,2,0,0,0]
arr3 = []

def is_jumpable(arr, start_index=None):
    if not arr: # no elements / invalid input
        return False

    start_index = start_index if start_index else 0

    # can jump "outside" of the array
    if arr[start_index] + start_index >= len(arr):
        return True
    
    end_pos = start_index + arr[start_index]
    # +1 to make it inclusive of end position.
    possible_locations = range(start_index + 1, end_pos + 1)

    for location in possible_locations: # look at all possible places to jump from
        found_exit = is_jumpable(arr, location) # can exit from that position.
        if found_exit:
            return True

    return False   # tried all routes, no way to jump to the exit.
    
print("Arr: " + str(arr))
jumpable = is_jumpable(arr)
print(jumpable)
print("Arr: " + str(arr2))
jumpable = is_jumpable(arr2)
print(jumpable)
print("Arr: " + str(arr3))
jumpable = is_jumpable(arr3)
print(jumpable)