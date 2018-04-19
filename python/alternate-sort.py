"""

Description:
Write a function

alternate_sort(l)
that combines the elements of an array by sorting the elements ascending by their absolute value and outputs negative and non-negative integers alternatingly (starting with the negative value, if any).

E.g.

alternate_sort([5, -42, 2, -3, -4, 8, -9,]) == [-3, 2, -4, 5, -9, 8, -42]
alternate_sort([5, -42, 2, -3, -4, 8, 9]) == [-3, 2, -4, 5, -42, 8, 9]
alternate_sort([5, 2, -3, -4, 8, -9]) == [-3, 2, -4, 5, -9, 8]
alternate_sort([5, 2, 9, 3, 8, 4]) == [2, 3, 4, 5, 8, 9]

"""


def alternate_sort(l):
    neg = sorted([n for n in l if n < 0], reverse=True)
    pos = sorted([n for n in l if n >= 0])
    res = []

    longer = neg if len(neg) > len(pos) else pos
    shorter = neg if longer == pos else pos

    for n, p in zip(neg, pos):
        res.append(n)
        res.append(p)

    for rest in longer[len(shorter):]:
        res.append(rest)

    return res
