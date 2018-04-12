"""

Description:
Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

your_order("is2 Thi1s T4est 3a")
[1] "Thi1s is2 3a T4est

"""


import re


def order(sentence):
    split_sentence = sentence.split()
    # initialize new list with the correct size
    new_order = [None] * len(split_sentence)

    for word in split_sentence:
        # identify the digit and subtract to meet index
        digit = int(re.search("(\d+)", word).group(1)) - 1
        new_order[digit] = word  # fill up the result list

    return " ".join(new_order)
