"""
Description:
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

#Example: longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

"""


def longest_consec(strarr, k):
    if len(strarr) == 0 or k <= 0 or k > len(strarr):
        return ""

    if k == 1:
        return max(strarr, key=lambda s: len(s))

    highest_sum = 0
    highest_index = -1
    for i in range(len(strarr)):
        current_sum = 0
        to = i + k
        if i + k >= len(strarr):
            to = len(strarr)

        for j in range(i, to):
            current_sum += len(strarr[j])

        if current_sum > highest_sum:
            highest_sum = current_sum
            highest_index = i

    return "".join(strarr[highest_index:highest_index + k])
