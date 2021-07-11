class SimpleSymbols {
    public static String SimpleSymbols(String str) {
        for (int i = 0; i < str.length(); i++) {
            char letter = str.charAt(i);
            if (Character.isLetter(letter)) {
                // check before and after for +
                if (i == 0 || i == str.length() - 1) {
                    return "false"; // can't have a + before it if it's the first character or after if it's the last
                }

                if (str.charAt(i - 1) != '+' || str.charAt(i + 1) != '+') {
                    return "false"; // the character isn't surrounded by plusses
                }
            }
        }
        return "true";
    }
}
