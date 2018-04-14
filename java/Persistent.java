/*
Description:
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) == 3 // because 3*9 = 27, 2*7 = 14, 1*4=4
                      // and 4 has only one digit

 persistence(999) == 4 // because 9*9*9 = 729, 7*2*9 = 126,
                       // 1*2*6 = 12, and finally 1*2 = 2

 persistence(4) == 0 // because 4 is already a one-digit number
*/

class Persist {
    public static int persistence(long n) {

        if (n < 10) {
            return 0;
        }

        String s = "" + n;
        int result = digitsMultiplied(s);
        int numSteps = 1;
        while (result >= 10) {
            s = "" + result;
            result = digitsMultiplied(s);
            numSteps++;
        }
        return numSteps;
    }

    private static int digitsMultiplied(String s) {
        int result = Character.getNumericValue(s.charAt(0));
        for (int i = 1; i < s.length(); i++) {
            result *= Character.getNumericValue(s.charAt(i));
        }
        return result;
    }
}