#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 15:21:18 2025

@author: arnavgupta
"""
"""
from string import ascii_lowercase
import unittest

def createTable(phrase):
    phrase = phrase.lower()
    phrase = "".join(filter(str.isalpha, phrase)).replace("q", "")
    seen = set()
    unique_phrase = "".join([c for c in phrase if not (c in seen or seen.add(c))])
    remaining_letters = "".join([c for c in ascii_lowercase if c not in unique_phrase and c != "q"])
    final_string = unique_phrase + remaining_letters
    return [list(final_string[i:i+5]) for i in range(0, 25, 5)]

def splitString(plaintext):
    plaintext = plaintext.lower()
    plaintext = "".join(filter(str.isalpha, plaintext)).replace("q", "")
    pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            pairs.append(plaintext[i] + 'x')
            break
        if plaintext[i] == plaintext[i + 1]:
            pairs.append(plaintext[i] + 'x')
            i += 1
        else:
            pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    return pairs

def findPosition(letter, table):
    for r, row in enumerate(table):
        if letter in row:
            return r, row.index(letter)

def playfairRuleOne(pair):
    if pair[0] == pair[1]:
        return pair[0] + ('x' if pair[0] != 'x' else 'z')
    return pair

def playfairRuleTwo(pair, table):
    r1, c1 = findPosition(pair[0], table)
    r2, c2 = findPosition(pair[1], table)
    if r1 == r2:
        return table[r1][(c1 + 1) % 5] + table[r2][(c2 + 1) % 5]
    return pair

def playfairRuleThree(pair, table):
    r1, c1 = findPosition(pair[0], table)
    r2, c2 = findPosition(pair[1], table)
    if c1 == c2:
        return table[(r1 + 1) % 5][c1] + table[(r2 + 1) % 5][c2]
    return pair

def playfairRuleFour(pair, table):
    r1, c1 = findPosition(pair[0], table)
    r2, c2 = findPosition(pair[1], table)
    if r1 != r2 and c1 != c2:
        return table[r1][c2] + table[r2][c1]
    return pair

def encrypt(pair, table):
    pair = playfairRuleOne(pair)
    pair = playfairRuleTwo(pair, table)
    pair = playfairRuleThree(pair, table)
    pair = playfairRuleFour(pair, table)
    return pair

def joinPairs(pairsList):
    return "".join(pairsList)

def main():
    table = createTable("i am entering a pass phrase")
    splitMessage = splitString("this is a test message")
    pairsList = [encrypt(pair, table) for pair in splitMessage]
    cipherText = joinPairs(pairsList)
    print(cipherText)

class TestPlayfair(unittest.TestCase):
    def test_createTable(self):
        self.assertEqual(createTable("i am entering a pass phrase"),
                         [['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z']])
    def test_splitString(self):
        self.assertEqual(splitString("this is my plaintext"), ["th", "is", "is", "my", "pl", "ai", "nt", "ex", "tx"])
    def test_playfairRuleOne(self):
        self.assertEqual(playfairRuleOne("gg"), "gx")
        self.assertEqual(playfairRuleOne("xx"), "xz")
    def test_encrypt(self):
        table = createTable("i am entering a pass phrase")
        self.assertEqual(encrypt("gg", table), "cm")

if __name__ == "__main__":
    unittest.main()
"""