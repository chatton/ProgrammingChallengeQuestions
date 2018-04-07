import java.util.*;
import java.io.*;

// CoderByte challenge

class Main {

    public static boolean isVowel(char c) {
        return "aeiou".indexOf(c) >= 0;
    }

    public static String LetterChanges(String str) {

        StringBuilder result = new StringBuilder();

        for (char c : str.toCharArray()) {
            if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                char newChar = c == 'z' ? 'a' : (char) ((int) c + 1);
                if (isVowel(newChar)) {
                    newChar = Character.toUpperCase(newChar);
                }
                result.append(newChar);
            } else {
                result.append(c);
            }
        }

        return result.toString();
    }

}
