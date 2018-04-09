/*

Description:
#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

*/

function findMissingLetter(array) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const startIndex = alphabet.indexOf(array[0]);
    const endIndex = alphabet.indexOf(array[array.length - 1]);
    const alphaSegment = alphabet.substring(startIndex, endIndex + 1);

    // find difference in strings using sets
    const set1 = new Set(alphaSegment.split(""));
    const set2 = new Set(array);
    const diff = new Set([...set1].filter(x => !set2.has(x)));

    return diff.values().next().value
}