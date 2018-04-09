/*

Description:
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

*/

function findOdd(A) {
    const counts = new Map();
    for (let number of A) {
        const num = counts.get(number) || 0;
        counts.set(number, num + 1);
    }

    for (let number of A) {
        if (counts.get(number) % 2 == 1) {
            return number
        }

    }
    return 0;
}