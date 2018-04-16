def unique(integers):
    seen = set()
    result = []
    for i in integers:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
