

def balance_check(s):
    opening = {
        "(": 1,
        "{": 2,
        "[": 3
    }
    closing = {
        ")": 1,
        "}": 2,
        "]": 3
    }

    open_stack = []
    for paren in s:
        if paren in opening:
            open_stack.append(paren)

        if paren in closing:
            if not open_stack:  # seeing a closing before an opening, can't be true
                return False

            # the closing is matching the last opening
            if closing[paren] != opening[open_stack.pop()]:
                return False

    return True


assert balance_check("{[]}") is True
assert balance_check("{([])}") is True
assert balance_check("{([]})") is False
assert balance_check("{([[{}]])}") is True
assert balance_check("([])}") is False
