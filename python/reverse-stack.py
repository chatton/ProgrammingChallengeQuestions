def reverse(stack):
    if not stack:
        return stack
    temp = stack.pop()
    reverse(stack)
    _insert_at_bottom(stack, temp)


def _insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return

    temp = stack.pop()
    _insert_at_bottom(stack, item)
    stack.append(temp)


stack = [1, 2, 3, 4, 5]
reverse(stack)
print(stack)
