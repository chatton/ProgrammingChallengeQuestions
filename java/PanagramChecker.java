/*

Description:
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
*/


import java.util.*;

public class PanagramChecker {
    public boolean check(String sentence) {
        sentence = sentence.toLowerCase();
        Set<Character> alpha = new HashSet();
        Set<Character> seen = new HashSet();
        for (Character c : "abcdefghijklmnopqrstuvwxyz".toCharArray()) {
            alpha.add(c);
        }

        for (Character c : sentence.toCharArray()) {
            if (alpha.contains(c)) {
                seen.add(c);
            }
        }
        return seen.size() == 26;
    }
}
