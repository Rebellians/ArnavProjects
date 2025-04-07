"""Practice with writing test cases and performing test-driven development using a
Guess-My-Number game as a problem statement.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Arnav Gupta
"""

#Sorry for being late, electricity issues

import random

def computerNumber():
    return random.randint(1, 100)

def makeSmartGuess(lowest, highest, lastFeedback=None):
    return (lowest + highest) // 2

def provideFeedback(guess, theNum):
    if guess < theNum:
        feedback = "too low"
        return "too low"
    elif guess > theNum:
        feedback = "too high"
        return "too high"
    else:
        feedback = "correct"
        return "correct"
    
    print(f"Guess: {guess} : {feedback}")
    return feedback

def gameLoop():
    def helper(lowest, highest, target, guess_count):
        guess = makeSmartGuess(lowest, highest)
        guess_count += 1
        feedback = provideFeedback(guess, target)
        print(f"Guess {guess_count}: {guess} : {feedback}")
        if feedback == "correct":
            print(f"Finally! The number was {target}. It took {guess_count} guesses.")
            return guess_count
        elif feedback == "too low":
            return helper(guess + 1, highest, target, guess_count)
        else:
            return helper(lowest, guess - 1, target, guess_count)
    
    return helper(1, 100, computerNumber(), 0)


###############################################################
######TEST CASES BELOW INCLUDING THE GIVEN AND THE TWO I CAME UP WITH

#Given Test Case testing computernumber()
def testGeneratedNumber():
    for i in range(1000):
        aNum = computerNumber()
        assert 1 <= aNum <= 100, "Generated number is out of range"
        assert isinstance(aNum, int), "Generated number is not an integer"

#Coded Test Case #1
def testMakeSmartGuess():
    assert makeSmartGuess(1, 100) == 50, "Smart guess should start in the middle"
    assert makeSmartGuess(30, 60) == 45, "Smart guess should adapt based on range"
    assert isinstance(makeSmartGuess(1, 100), int), "Smart guess should be an integer"
    
#Coded Test Case #2        
def testGameLoop():
    for i in range(100):
        assert gameLoop() > 0 #tests (asserts) that the result is always greater than zero; tests game loop    

###############################################################

import unittest

####TEST PROVIDE FEEDBACK BELOW

class TestGuessMyNumber(unittest.TestCase):
    def testProvideFeedbackLow(self):
        self.assertEqual(provideFeedback(20, 50), "too low")
    
    def testProvideFeedbackHigh(self):
        self.assertEqual(provideFeedback(80, 50), "too high")
    
    def testProvideFeedbackCorrect(self):
        self.assertEqual(provideFeedback(50, 50), "correct")

    def aUtilityFunction(self, param):
    # This is a utility function which unittest.main() will NOT run automatically.
    # Your test functions could still use it though:
        self.aUtilityFunction("hello")
        print("Utility function runs! Has parameter:", param)


################################################################

def main():
    print("Running basic tests...")
    testGeneratedNumber()
    testMakeSmartGuess()
    testGameLoop()
    print("Basic tests passed!")
    print("Running structured tests...")
    unittest.main()
    print("Structured tests completed.")

if __name__ == "__main__":
    main()