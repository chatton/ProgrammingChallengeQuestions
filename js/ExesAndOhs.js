/*
Description:
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
*/

function XO(str) {
    const counts = new Map();
    for (let char of str) {
        char = char.toLowerCase();
        const amount = counts.get(char) || 0;
        counts.set(char, amount + 1);
    }

    if (counts.get("x") === undefined
        && counts.get("o") === undefined) {
        return true;
    }

    return counts.get("x") === counts.get("o");
}