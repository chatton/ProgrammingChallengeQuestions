public class StringCompression {

	public static void main(String... args) {

		String s1 = "aaaabbbbbcccdeeeeeeeee";
		String s2 = "abcde";
		String s3 = "";
		String s4 = "abbbccccddddeee";
		String s5 = "aaaa";

		assert compress(s1).equals("a4b5c3de9");
		assert compress(s2).equals("abcde");
		assert compress(s3).equals("");
		assert compress(s4).equals("ab3c4d4e3");
		assert compress(s5).equals("a4");

	}

	public static String compress(String input) {

		if (input.length() <= 1) { // nothing to compress
			return input;
		}
		final StringBuilder sb = new StringBuilder();
		int charCount = 1;
		for (int i = 0; i < input.length() - 1; i++) {
			char c = input.charAt(i);
			// look ahead one character and see if it's the same
			if (input.charAt(i + 1) == c) {
				charCount++; // one more of that char
			} else { // reached a new character
				sb.append(c); // add to the string
				if (charCount > 1) { // only add a number if it's more than 1
					sb.append(charCount);
				}
				charCount = 1; // reset the count.
			}
		}

		// need to account for the last character and count.
		sb.append(input.charAt(input.length() - 1));
		if (charCount > 1) {
			sb.append(charCount);
		}

		return sb.toString();
	}

}