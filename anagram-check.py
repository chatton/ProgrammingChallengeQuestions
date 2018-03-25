def is_anagram(s1, s2):
    counts = {}
    for letter in s1:
        num = counts.get(letter, 0) + 1
        counts[letter] = num

    for letter in s2:
        num = counts.get(letter, 0) - 1
        counts[letter] = num

    for letter in counts:
        if counts[letter] != 0:
            return False
    return True


print(is_anagram("dog", "god"))
print(is_anagram("dog", "gods"))