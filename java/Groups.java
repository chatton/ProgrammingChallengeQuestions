
/*

Description:
In English and programming, groups can be made using symbols such as () and {} that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]
The next are done incorrectly:

{(})
([]
[])
A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols (), {} or [] to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.

*/

import java.util.*;

public class Groups {

    public static boolean groupCheck(String s) {
        String opening = "({[";
        String closing = ")}]";

        Stack<Character> chars = new Stack<>();

        if (s.length() % 2 == 1) {
            return false;
        }

        int totalChars = s.length();
        for (Character c : s.toCharArray()) {

            if (closing.indexOf(c) >= 0) {
                totalChars--;
                int closingIndex = closing.indexOf(c);
                Character top = chars.pop();
                int openingCharIndex = opening.indexOf(top);

                System.out.println(openingCharIndex);
                System.out.println(closingIndex);

                if (openingCharIndex != -1 && openingCharIndex != closingIndex) {

                    return false;
                }
            }

            if (opening.indexOf(c) >= 0) {
                chars.push(c);
                totalChars--;
            }
        }
        return totalChars == 0;
    }

}