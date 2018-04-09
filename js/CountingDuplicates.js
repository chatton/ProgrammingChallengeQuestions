/*

Description:
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (bandB)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

*/

function duplicateCount(text) {
    text = text.toLowerCase();

    const counts = new Map();
    for (let letter of text) {
        const num = counts.get(letter) || 0;
        counts.set(letter, num + 1);
    }

    const set = new Set();
    for (let letter of text) {
        if (counts.get(letter) >= 2) {
            set.add(letter);
        }
    }

    return set.size;
}