function firstUnique(s) {
    if (typeof s !== "string") {
        return;
    }

    const counts = new Map();

    for (let i = 0; i < s.length; i++) {
        const letter = s.charAt(i);
        const num = counts.get(letter) || 0;
        counts.set(letter, num + 1);
    }

    for (let i = 0; i < s.length; i++) {
        const letter = s.charAt(i);
        if (counts.get(letter) === 1) {
            return letter;
        }
    }
}


console.log(firstUnique("aabccccd")); // b
console.log(firstUnique(null)); // undefined
console.log(firstUnique(1)); // undefined
console.log(firstUnique("aabbcc")); // undefined
console.log(firstUnique("aabbccdef")); // d