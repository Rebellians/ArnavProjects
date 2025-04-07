# -*- coding: utf-8 -*-
"""
Functions about word reductions

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: ARNAV GUPTA
"""
__version__ = 33

def loadWords():
    '''
    This function opens the words_alpha.txt file, reads it
    line-by-line, and adds each word into a list.  It returns
    the list containing all words in the file.
    '''
    with open('words_alpha.txt') as wordFile:
        wordList = set(line.strip() for line in wordFile)  # Using set for faster lookups
    return wordList


def reduceOne(firstString, secondString, wordList):
    """
    Tests whether firstString can reduce to secondString.
    firstString and secondString must both be valid words from wordList, and firstString must also reduce
    to secondString by removing a single character from firstString.
    """
    if firstString not in wordList or secondString not in wordList or len(secondString) != len(firstString) - 1:
        return False

    for i in range(len(firstString)):
        temp_string = firstString[:i] + firstString[i+1:]
        if temp_string == secondString:
            return True

    return False

def reduceAll(word, wordList):
    """
    Creates a collection of strings that can be reduced from a provided string word.
    """
    reduced_words = []
    for i in range(len(word)):  # Iterate through each character index
        reduced_word = word[:i] + word[i+1:]  
        if reduced_word in wordList:
            reduced_words.append(reduced_word)

    return reduced_words

def reduceTwoAll(word, wordList):
    """
    Creates a collection of strings that can be reduced from a provided string
    word by removing TWO characters.
    """
    twice_reduced_words = []
    for i in range(len(word)):
        intermediate_word = word[:i] + word[i+1:]  # Reduce by one character.. could've called reduceAll instead ik
        for j in range(len(intermediate_word)):
            reduced_word = intermediate_word[:j] + intermediate_word[j+1:]  # Reduces again... once again could've called reduceAll
            if reduced_word in wordList: 
                twice_reduced_words.append(reduced_word)

    return twice_reduced_words

def validateReduction(reduction, wordList):
   """
   Confirms whether or not an input list reduction represents a valid
   sequence of reductions.
   """
   if len(reduction) == 1: #If only one word, and it's in the wordlist... it's valid
        return reduction[0] in wordList

   for i in range(len(reduction) - 1):
        current_word = reduction[i]
        next_word = reduction[i+1]

        if current_word not in wordList or next_word not in wordList:
            return False

        possible_reductions = reduceAll(current_word, wordList)

        if next_word not in possible_reductions:
            return False
        return True

def main():
    wordList = loadWords()
    run_tests(wordList)

def run_tests(wordList):
    test1(wordList)
    test2(wordList)
    test3(wordList)
    test4(wordList)
    test5(wordList)
    test6(wordList)
    test7(wordList)
    test8(wordList)
    test9(wordList)
    test10(wordList)
    test11(wordList)
    test12(wordList)
    test13(wordList)
    test14(wordList)
    test15(wordList)
    test16(wordList)
    print("All tests passed!")

############################################################### TEST CASES

def test1(wordList):
    assert reduceOne("leave", "eave", wordList) == True # Test if "leave" can be reduced to "eave"

def test2(wordList):
    assert reduceOne("leave", "leav", wordList) == False # Test if "leave" can be reduced to "leav"

def test3(wordList):
    assert reduceOne("stone", "tone", wordList) == True # Test if "stone" can be reduced to "tone"

def test4(wordList):
    assert reduceOne("apple", "aple", wordList) == False # Test if "apple" can be reduced to "aple"

def test5(wordList):
    assert "boat" in reduceAll("boats", wordList) # Test if "boat" is among the reductions of "boats"

def test6(wordList):
    assert "oats" in reduceAll("boats", wordList) # Test if "oats" is among the reductions of "boats"
    
def test7(wordList):
    assert "oats" not in reduceAll("plane", wordList) # Test if "oats" is NOT among the reductions of "plane"

def test8(wordList):
    assert "aots" not in reduceAll("boat", wordList) # Test if "aots" is NOT among the reductions of "boat"
    
def test9(wordList):
    assert "rie" in reduceTwoAll("eerie", wordList) # Test if "rie" is among the two-character reductions of "eerie"   
    
def test10(wordList):
    assert "eer" in reduceTwoAll("eerie", wordList) # Test if "eer" is among the two-character reductions of "eerie"  
    
def test11(wordList):
    assert "eer" not in reduceTwoAll("carry", wordList) # Test if "eer" is NOT among the two-character reductions of "carry"  
    
def test12(wordList):
    assert "pair" not in reduceTwoAll("pear", wordList) # Test if "pair" is NOT among the two-character reductions of "pear"
    
def test13(wordList):
    assert validateReduction(["turntables", "turntable", "tunable", "unable"], wordList) == True # Test if the reduction sequence is valid
    
def test14(wordList):
    assert validateReduction(["turntables", "table", "able"], wordList) == False # Test if the reduction sequence is invalid
    
def test15(wordList):
    assert validateReduction(["crane", "cane", "can", "an", "a"], wordList) == True # Test if the reduction sequence is valid
    
def test16(wordList):
    assert validateReduction(["planet", "plane", "plan", "pan", "at"], wordList) == True # Test if the reduction sequence is valid
    
###############################################################

if __name__ == "__main__":
    main()