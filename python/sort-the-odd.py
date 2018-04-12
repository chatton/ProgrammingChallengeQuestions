"""

Description:
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

"""


def sort_array(source_array):
    if not source_array:
        return []

    new_arr = sorted(list(filter(lambda x: x % 2 == 1, source_array)))
    current_index = 0

    result = list(source_array)

    for x in range(len(source_array)):
        if source_array[x] % 2 == 1:
            result[x] = new_arr[current_index]
            current_index += 1

    return result
