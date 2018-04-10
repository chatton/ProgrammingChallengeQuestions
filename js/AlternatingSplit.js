/*

Description:
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

function encrypt(text, n)
function decrypt(encryptedText, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

*/

function encrypt(text, n) {
    if (!text || n <= 0) {
        return text;
    }

    for (let i = 0; i < n; i++) {
        const chars = [];
        for (let j = 0; j < text.length; j++) {
            const letter = text.charAt(j);
            chars.push({
                val: letter,
                even: j % 2 == 0
            });
        }
        const firstPart = chars.filter(l => !l.even).map(l => l.val);
        const secondPart = chars.filter(l => l.even).map(l => l.val);
        text = firstPart.concat(secondPart).join("");
    }

    return text;
}

function decrypt(encryptedText, n) {
    if (!encryptedText || n <= 0) {
        return encryptedText;
    }

    for (let i = 0; i < n; i++) {
        const firstHalf = encryptedText.substring(0, encryptedText.length / 2);
        const secondHalf = encryptedText.substring(encryptedText.length / 2, encryptedText.length);
        const chars = [];

        for (let j = 0; j < firstHalf.length; j++) {
            chars.push(secondHalf.charAt(j));
            chars.push(firstHalf.charAt(j));
        }

        if (secondHalf.length > firstHalf.length) {
            chars.push(secondHalf.charAt(secondHalf.length - 1));
        }

        encryptedText = chars.join("");
    }


    return encryptedText;

}