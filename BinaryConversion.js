/*

Description:
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

*/

const binaryArrayToNumber = arr => {
    let currentPower = arr.length - 1;
    let result = 0;
    for (let bin of arr) {
        if (bin === 1) {
            result += Math.pow(2, currentPower);
        }
        currentPower--;

    }
    return result;
};

  // one liner -  return parseInt(Number(arr.join('')), 2)