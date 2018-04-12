
def is_prime(num):

    if num in (-1, 0, 1):
        return False

    if num in (-2, 2):
        return True

    for x in range(2, num / 2 + 1):

        if num % x == 0:
            return False

    return True
