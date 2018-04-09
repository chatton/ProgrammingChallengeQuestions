/*

The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

###Examples:

tickets([25, 25, 50]) // => YES 
tickets([25, 100])    
        // => NO. Vasya will not have enough money to give change to 100 dollars

*/


function tickets(peopleInLine) {
    const ticketPrice = 25;
    const denominations = [100, 50, 25];

    // keep track of all the notes the bank has
    let bank = {
        "25": 0,
        "50": 0,
        "100": 0
    }

    for (let cashAmount of peopleInLine) {

        bank["" + cashAmount]++; // have one more note of this denomination

        let changeNeeded = cashAmount - ticketPrice;
        for (let den of denominations) {
            while (bank["" + den] > 0 && changeNeeded >= den) {
                changeNeeded -= den;
                bank["" + den]--;
            }
        }

        const hadCorrectChange = changeNeeded === 0;

        if (!hadCorrectChange) {
            return "NO";
        }
    }

    return "YES";

}