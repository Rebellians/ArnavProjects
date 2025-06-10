/** Defining a Rational number class
Refer to the instructions on Canvas for more information.
"I have neither given nor received unauthorized help on this assignment."
author: Arnav Gupta
**/

public class Rational {

    // These are the instance variables defined for your class. Don't change these lines!
    private int numerator;
    private int denominator;

    /**
     * Initializes a new Rational object
     * Consumes two ints representing numerator and denominator
     * Returns a Rational in lowest terms
     */
    public Rational(int iNum, int iDen) {
        this.numerator = iNum;
        this.denominator = iDen;
        this.reduce();
    }

    /**
     * Gets the numerator of the Rational number
     * Consumes nothing
     * Returns an int
     */
    public int getNumerator() {
        return this.numerator;
    }

    /**
     * Gets the denominator of the Rational number
     * Consumes nothing
     * Returns an int
     */
    public int getDenominator() {
        return this.denominator;
    }

    /**
     * Checks if the Rational number is valid (denominator is not zero)
     * Consumes nothing
     * Returns a boolean
     */
    public boolean isValid() {
        return this.denominator != 0;
    }

    /**
     * Creates a new Rational that is the reciprocal of the current one
     * Consumes nothing
     * Returns a Rational
     */
    public Rational reciprocal() {
        if (this.numerator == 0) {
            throw new ArithmeticException("Cannot take reciprocal of zero");
        }
        return new Rational(this.denominator, this.numerator);
    }

    /**
     * Adds the current Rational to another Rational
     * Consumes a Rational
     * Returns a new Rational representing the sum
     */
    public Rational add(Rational num2) {
        int newNumerator = this.numerator * num2.getDenominator() + num2.getNumerator() * this.denominator;
        int newDenominator = this.denominator * num2.getDenominator();
        return new Rational(newNumerator, newDenominator);
    }

    /**
     * Subtracts another Rational from the current Rational
     * Consumes a Rational
     * Returns a new Rational representing the difference
     */
    public Rational sub(Rational num2) {
        int newNumerator = this.numerator * num2.getDenominator() - num2.getNumerator() * this.denominator;
        int newDenominator = this.denominator * num2.getDenominator();
        return new Rational(newNumerator, newDenominator);
    }

    /**
     * Multiplies the current Rational by another Rational
     * Consumes a Rational
     * Returns a new Rational representing the product
     */
    public Rational mult(Rational num2) {
        int newNumerator = this.numerator * num2.getNumerator();
        int newDenominator = this.denominator * num2.getDenominator();
        return new Rational(newNumerator, newDenominator);
    }

    /**
     * Divides the current Rational by another Rational
     * Consumes a Rational
     * Returns a new Rational representing the quotient
     */
    public Rational div(Rational num2) {
        if (num2.getNumerator() == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        int newNumerator = this.numerator * num2.getDenominator();
        int newDenominator = this.denominator * num2.getNumerator();
        return new Rational(newNumerator, newDenominator);
    }

    /**
     * Compares two Rational numbers to see if the current one is less than the other
     * Consumes a Rational
     * Returns a boolean
     */
    public boolean isLessThan(Rational num2) {
        int left = this.numerator * num2.getDenominator();
        int right = num2.getNumerator() * this.denominator;
        return left < right;
    }


 /*******************************
 *    HELPER FUNCTIONS BELOW    *
 *******************************/

    /**
     * Reduces the Rational number to lowest terms
     * Consumes nothing
     * Returns nothing
     */
    private void reduce() {
        if (this.denominator < 0) {
            this.numerator = -this.numerator;
            this.denominator = -this.denominator;
        }
        int common = this.gcf();
        this.numerator = numerator / common;
        this.denominator = denominator / common;
    }

    /**
     * Finds the greatest common factor of the numerator and denominator
     * Consumes nothing
     * Returns an int
     */
    private int gcf() {
        int absNum = Math.abs(numerator);
        int absDen = Math.abs(denominator);
        int minOfNums = Math.min(absNum, absDen);
        for (int i = minOfNums; i > 0; i--) {
            if (numerator % i == 0 && denominator % i == 0) {
                return i;
            }
        }
        return 1;
    }

    /**
     * Returns the Rational number as a string in the format numerator/denominator
     * Consumes nothing
     * Returns a String
     */
    public String toString() {
        return this.numerator + "/" + this.denominator;
    }

    /**
     * Checks if the current Rational is equal to another object
     * Consumes an Object
     * Returns a boolean
     */
    public boolean equals(Object other) {
        if (!(other instanceof Rational)) return false;
        Rational fraction = (Rational) other;
        int otherNum = fraction.getNumerator();
        int otherDen = fraction.getDenominator();
        return this.numerator == otherNum && this.denominator == otherDen;
    }

    /**
     * Main method that prints instructions about running the test file
     * Consumes an array of Strings
     * Returns nothing
     */
    public static void main(String[] args) {
        System.out.println("You're running the Rational.java file.");
        System.out.println("If you want to test your program,");
        System.out.println("you should run the RationalTest.java file instead!");
    }

} // Rational (class)