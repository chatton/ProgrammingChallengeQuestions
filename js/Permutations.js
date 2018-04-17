/*

Description:
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); // ['a']
permutations('ab'); // ['ab', 'ba']
permutations('aabb'); // ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.

*/

function permutations(s) {
  const result = new Set();
  perms("", s, result);
  return Array.from(result);
}

function perms(prefix, suffix, set) {
  if (suffix.length == 0) {
    set.add(prefix);
  } else {
    for (let i = 0; i < suffix.length; i++) {
      perms(
        prefix + suffix.charAt(i),
        suffix.substring(0, i) + suffix.substring(i + 1, suffix.length),
        set
      );
    }
  }
}
