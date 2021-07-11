
/*

Description:
Create a function isAlt() that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

isAlt("amazon")
// true
isAlt("apple")
// false
isAlt("banana")
// true
Arguments consist of only lowercase letters.

*/

import java.util.*;

public class AreWeAlternate {
    public static boolean isAlt(String word) {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        char[] vowelsArr = "aeiou".toCharArray();
        Set<Character> vowels = new HashSet<>();
        for (Character c : vowelsArr) {
            vowels.add(c);
        }

        Set<Character> consonants = new HashSet<>();
        for (Character c : alphabet) {
            if (!vowels.contains(c)) {
                consonants.add(c);
            }
        }

        boolean startsWithVowel = vowels.contains(word.charAt(0));

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (i % 2 == 0) {
                if (startsWithVowel ? !vowels.contains(c) : !consonants.contains(c)) {
                    return false;
                }
            } else {
                if (startsWithVowel ? !consonants.contains(c) : !vowels.contains(c)) {
                    return false;
                }
            }
        }
        return true;
    }
}
