import junit.framework.TestCase;

/** The RationalTest unit test class.
Refer to the instructions on Canvas for more information.
"I have neither given nor received unauthorized help on this assignment."
author: ARNAV GUPTA
**/

public class RationalTest extends TestCase {

    public void testToString() {
        assertEquals("4/7", new Rational(4, 7).toString());
        assertEquals(5, 2 + 3);
    }

    public void testNullAndBoolean() {
        Rational r = null;
        assertNull(r);
        assertNotNull(new Rational(3, 5));
        assertTrue(3 == 1 + 2);
        assertTrue("this message is for when an assertion fails", 3 == 1 + 2);
    }

    public void testGetNumerator() {
        // Tests getNumerator(): consumes no input, returns int numerator of Rational(3, 4)
        assertEquals(3, new Rational(3, 4).getNumerator());
    }

    public void testInitialization() {
        // Tests constructor and getNumerator(): consumes int numerator and denominator, returns reduced numerator as int
        assertEquals(3, new Rational(3, 4).getNumerator());
        // Tests getDenominator(): consumes no input, returns denominator as int
        assertEquals(4, new Rational(3, 4).getDenominator());

        // Tests zero numerator: consumes 0 and int denominator, returns 0 as numerator
        assertEquals(0, new Rational(0, 5).getNumerator());
        assertEquals(5, new Rational(0, 5).getDenominator());

        // Tests rational equal to 1: consumes equal numerator and denominator, returns 1/1
        assertEquals(1, new Rational(5, 5).getNumerator());
        assertEquals(1, new Rational(5, 5).getDenominator());
    }

    public void testReduction() {
        // Tests reduction of Rational(15, 25) to lowest terms: returns 3/5
        assertEquals(3, new Rational(15, 25).getNumerator());
        assertEquals(5, new Rational(15, 25).getDenominator());

        // Tests reduction of Rational(6, 8) to 3/4
        assertEquals(3, new Rational(6, 8).getNumerator());
        assertEquals(4, new Rational(6, 8).getDenominator());

        // Tests reduction of Rational(5, 10) to 1/2
        assertEquals(1, new Rational(5, 10).getNumerator());
        assertEquals(2, new Rational(5, 10).getDenominator());
    }

    public void testNegativeDenominatorReduction() {
        // Tests normalization of negative denominator: Rational(5, -7) becomes -5/7
        assertEquals(-5, new Rational(5, -7).getNumerator());
        assertEquals(7, new Rational(5, -7).getDenominator());

        // Tests double negatives: Rational(-3, -4) becomes 3/4
        assertEquals(3, new Rational(-3, -4).getNumerator());
        assertEquals(4, new Rational(-3, -4).getDenominator());

        // Tests zero numerator with negative denominator: Rational(0, -2) becomes 0/2
        assertEquals(0, new Rational(0, -2).getNumerator());
        assertEquals(2, new Rational(0, -2).getDenominator());
    }

    public void testIsValid() {
        // Tests isValid(): consumes Rational, returns boolean indicating denominator != 0
        assertTrue(new Rational(3, 4).isValid());
        assertFalse(new Rational(2, 0).isValid());
        assertTrue(new Rational(1, 5).isValid());
    }

    public void testReciprocal() {
        // Tests reciprocal(): consumes Rational(4, 9), returns Rational(9, 4)
        assertEquals(9, new Rational(4, 9).reciprocal().getNumerator());
        assertEquals(4, new Rational(4, 9).reciprocal().getDenominator());

        // Tests reciprocal() on zero numerator: should throw ArithmeticException
        try {
            new Rational(0, 5).reciprocal();
            fail("Expected ZeroDivisionError");
        } catch (ArithmeticException e) {
        
        }
    }

    public void testAdd() {
        // Tests add(): consumes two Rationals, returns their sum as a reduced Rational
        assertEquals(9, new Rational(3, 5).add(new Rational(6, 5)).getNumerator());
        assertEquals(5, new Rational(3, 5).add(new Rational(6, 5)).getDenominator());

        assertEquals(5, new Rational(1, 2).add(new Rational(1, 3)).getNumerator());
        assertEquals(6, new Rational(1, 2).add(new Rational(1, 3)).getDenominator());

        assertEquals(1, new Rational(-1, 4).add(new Rational(3, 8)).getNumerator());
        assertEquals(8, new Rational(-1, 4).add(new Rational(3, 8)).getDenominator());
    }

    public void testSub() {
        // Tests sub(): consumes two Rationals, returns their difference as a reduced Rational
        assertEquals(1, new Rational(7, 8).sub(new Rational(3, 8)).getNumerator());
        assertEquals(2, new Rational(7, 8).sub(new Rational(3, 8)).getDenominator());

        assertEquals(7, new Rational(5, 6).sub(new Rational(1, 4)).getNumerator());
        assertEquals(12, new Rational(5, 6).sub(new Rational(1, 4)).getDenominator());

        assertEquals(1, new Rational(1, 3).sub(new Rational(1, 6)).getNumerator());
        assertEquals(6, new Rational(1, 3).sub(new Rational(1, 6)).getDenominator());
    }

    public void testMult() {
        // Tests mult(): consumes two Rationals, returns product as reduced Rational
        assertEquals(9, new Rational(3, 4).mult(new Rational(6, 5)).getNumerator());
        assertEquals(10, new Rational(3, 4).mult(new Rational(6, 5)).getDenominator());

        assertEquals(-2, new Rational(-1, 2).mult(new Rational(4, 3)).getNumerator());
        assertEquals(3, new Rational(-1, 2).mult(new Rational(4, 3)).getDenominator());

        assertEquals(1, new Rational(2, 7).mult(new Rational(7, 2)).getNumerator());
        assertEquals(1, new Rational(2, 7).mult(new Rational(7, 2)).getDenominator());
    }

    public void testDiv() {
        // Tests div(): consumes two Rationals, returns quotient as reduced Rational
        assertEquals(5, new Rational(3, 4).div(new Rational(6, 5)).getNumerator());
        assertEquals(8, new Rational(3, 4).div(new Rational(6, 5)).getDenominator());
    }

    public void testLessThan() {
        // Tests isLessThan(): consumes two Rationals, returns boolean if first < second
        assertTrue(new Rational(5, 6).isLessThan(new Rational(4, 3)));
        assertFalse(new Rational(1, 2).isLessThan(new Rational(1, 2)));
        assertTrue(new Rational(-1, 2).isLessThan(new Rational(1, 2)));
    }

    public String notATestJustAHelper() {
        return "I could return something useful?";
    }

    public void testStarterCode() {
        // Tests main() and toString(): ensures Rational can be created and printed, returns non-null string
        Rational.main(null);
        assertNotNull(new Rational(1, 1).toString());
        // Tests equals(): consumes another Rational, returns true if both have same value
        assertTrue(new Rational(1, 1).equals(new Rational(1, 1)));
    }
}
