from itertools import permutations


def next_bigger(n):
    biggest_possible = int(''.join(sorted(str(n), reverse=True)))
    if n == biggest_possible:
        return -1

    s = str(n)
    perms = permutations(s, len())
    possible_numbers = sorted(
        list(set([int(''.join(perm)) for perm in perms])))
    return possible_numbers[possible_numbers.index(n) + 1]
