/*

Note: This is my first Kata, so I'm really new to this :) Please vote and give feedback! Thanks, and have a fun time coding!

My friend Tim and I are huge fans of gladiators. We also really like games, so I thought to myself that we should have a game where we can create our own Gladiators and then make them fight against each other! Can you help us make this game?

A Gladiator has 5 important stats:

The name of the Gladiator, String
The health of the Gladiator, double
The damage of the Gladiator, int
The defense of the Gladiator, int
The initiative of the Gladiator, int
All the stats are really simple:

The initiative determines whether a gladiator will attack first in a battle. The gladiator with the higher initiative attacks first!
The health of a Gladiator represents how much life points he has left. If it drops to zero or below, the gladiator is defeated!
The damage of the gladiator determines how much health points a gladiator can remove with a single attack.
The defense stat allows a gladiator to ignore a certain amount of damage. With a defense of 10, he can ignore 10% of all incoming damage!
Lets see an example!

Spartacus: health 100, damage 30, defense 25, initiative 60
Gannicus: health 100, damage 40, defense 10, initiative 50
 Spartacus has higher initiative, so he starts 
Round 1: Spartacus does 30 damage, 10% of which Gannicus ignores. Gannicus has 73 health left.
Round 2: Gannicus does 40 damage, 25% of which Spartacus ignores. Spartacus has 70 health left.
Round 3: Spartacus does 30 damage, 10% of which Gannicus ignores. Gannicus has 46 health left.
...
Round 7: Spartacus does 30 damage, 10% of which Gannicus ignores. Gannicus has zero or less health --> Spartacus wins!
Easy, right? Now, for the technicalities... I would like to be able to create a Gladiator in the following way:

Gladiator(String name, double health, int damage, int defense, int initiative)
I would also like to be able to not specify the initiative. In this case, it should be zero.

The Gladiator should have getter methods for all 5 members, so we can check on our gladiators whenever we wish.

The Gladiator class should also have a static method which takes 2 gladiators, competes them in the above mentioned way, and returns the winning Gladiator!

public static Gladiator fight(Gladiator gladiator1, Gladiator gladiator2)
My friend Tim is a cheeky pal, I'm sure he will try to make Gladiators that make absolutely no sense just to make fun of my program, so we need to check the input parameters of the constructors. Make sure the constructors' arguments are valid, and if not, then throw an IllegalArgumentException.

name is invalid if empty or null
health is invalid if not positive - no sense in creating a dead gladiator, right?
damage should also be above zero - what's the point in a gladiator who can't do any damage? Not to mention one who does negative damage?
defense should be non-negative but smaller than 100. Not much fun playing against an invincible gladiator, right? Remember, 0 defense is valid!
Note:

If the initiative of both gladiators is the same in
public static Gladiator fight(Gladiator gladiator1, Gladiator gladiator2)
then the gladiator passed as the first argument (gladiator1) should begin.
Initiative determines who begins the fight, but afterwards the gladiators simply take turns attacking, as you can see in the example above!
When testing the fight method, only the name of the winner will be asserted
Though the base damage is an int, keep in mind that non-integer damages are possible because of the defense!
Have fun solving this Kata! Don't forget to vote and rank this Kata! Also, any feedback in the comments section is highly appreciated! ;)

*/

public class Gladiator {

    private final String name;
    private final int damage;
    private final int defense;
    private final int initiative;

    private double health;

    public Gladiator(String name, double health, int damage, int defense) {
        this(name, health, damage, defense, 0);
    }

    public Gladiator(String name, double health, int damage, int defense, int initiative) {
        validate(name, health, damage, defense);

        this.name = name;
        this.health = health;
        this.damage = damage;
        this.defense = defense;
        this.initiative = initiative;
    }

    private void validate(String name, double health, int damage, int defense) {
        if (name == null || name.trim().equals("")) {
            throw new IllegalArgumentException("Name must be non empty and non null");
        }

        if (health <= 0) {
            throw new IllegalArgumentException("Health must be > 0");
        }

        if (damage <= 0) {
            throw new IllegalArgumentException("Damage must be > 0");
        }

        if (defense < 0 || defense >= 100) {
            throw new IllegalArgumentException("Must have defense between 0 and 99");
        }
    }

    public String getName() {
        return name;
    }

    public double getHealth() {
        return health;
    }

    public int getDamage() {
        return damage;
    }

    public int getInitiative() {
        return initiative;
    }

    public int getDefense() {
        return defense;
    }

    public boolean isAlive() {
        return health > 0;
    }

    public void dealDamage(int damage) {
        double reduced = damage * (100.0 - defense);
        health -= reduced;
    }

    @Override
    public String toString() {
        return "[name=" + name + ",health=" + health + ",damage=" + damage + ",initiative=" + initiative + ",defense="
                + defense + "]";
    }

    public static Gladiator fight(Gladiator a, Gladiator b) {

        Gladiator current = b.initiative > a.initiative ? b : a;
        Gladiator target;

        do {
            target = current == a ? b : a;
            target.dealDamage(current.getDamage());

            current = target;
        } while (a.isAlive() && b.isAlive());

        return a.isAlive() ? a : b;
    }
}