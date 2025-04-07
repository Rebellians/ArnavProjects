#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:07:01 2025

@author: arnavgupta

"""

'''Functions about calendars

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."

author: YOUR NAME HERE
'''

def gregorian(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#Function above determines if a year is a Gregorian leap year

def milankovic(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 900 in {200, 600})
#Function above deterines if a year is a Milankovic leap year

def gregorian_count(year1, year2):
    return sum(gregorian(y) for y in range(year1, year2))
#Function above determines the number of leap years that lie between
#two dates on the Gregorian calendar

def milankovic_count(year1, year2):
    return sum(milankovic(y) for y in range(year1, year2))
#Function determines the number of leap years that lie between two dates
#on the Milankovic calendar

def fromMiddle(age, year):
    ageLengths = [None, 590, 3441, 3021, 2000, 2000, 2000]
    if age < 1 or age > 7:
        raise ValueError("Invalid Middle Earth age")
    modern_year = 1971
    for i in range(7, age, -1):
        modern_year -= ageLengths[i - 1]
    modern_year += year
    return modern_year
#Converts Middle Earth Age from LOR into a modern year

def toMiddle(year):
    ageLengths = [None, 590, 3441, 3021, 2000, 2000, 2000]
    middleYear = year - 1971
    age = 7
    while middleYear < 0 and age > 1:
        age -= 1
        middleYear += ageLengths[age]
    return (age, middleYear)
#Converts modern year into a Middle Earth Age from LOR

def main():
    #Webcat will ignore what's' here
    print("main is done")

############################################################ TEST CASES BELOW

import unittest

class TestCalendars(unittest.TestCase):
    #Tests leap years in the Greg. Calendar
    def testGregorian1(self):
        self.assertTrue(gregorian(1696), "gregorian year 1696 should be a leap year... function tests by returning true")
        self.assertFalse(gregorian(1700), "Should Not a leap year cus it's divisible by 100 but not by 400... function tests by returning false")
        self.assertTrue(gregorian(2000), "Should be a leap year cuz div by 400... functions should return True") 
                        
    def testMilankovic1(self):
    #Tests leap year in The Milankovic calendar
        self.assertTrue(milankovic(1696), "Milankovic year 1696 should be a leap year")
        self.assertFalse(milankovic(2800), "Milankovic year 2800 should not be a leap year")  
        self.assertTrue(milankovic(2400), "Milankovic year 2400 should be a leap year")                        
                         
    def testGregorianCount1(self):
    #Tests counting the number of leap yrs in Greg. over given periosd
        self.assertEqual(3, gregorian_count(1688, 1697), "1688 to 1697 should have 3 leap years in greg")
        self.assertEqual(0, gregorian_count(1900, 1901), "Should return error as no leap year between short time")
        self.assertEqual(243, gregorian_count(2000, 3000), "Tests if the function returns the appropriate # of leap yrs in 1000 yrs")
    
    def test_from_middle(self):
    #Tests conversion from Middle Earth Age to modern years
        self.assertEqual(fromMiddle(6, 1999), 1970) #Tests conversion from modern 1970 to Age 6, year 1999
        self.assertEqual(fromMiddle(7, 0), 1971) #Tests conversion from modern 1971 to Age 7, year 0
        self.assertEqual(fromMiddle(3, 2941), -4109) #Tests conversion from modern year 0
    
    def test_to_middle(self):
    #Tests conversion from modern years to Middle Earth
        self.assertEqual(toMiddle(1970), (6, 1999)) #Tests conversion from Age 6, 1999 to modern 1970
        self.assertEqual(toMiddle(1971), (7, 0)) #Tests conversion from Age 7, year 0 to modern 1971
        self.assertEqual(toMiddle(0), (6, 29), "toMiddle 0") #Ttesst conversion to modern year 0
        
    def test_milankovic_count_1(self):
    #Tests number of leap years over a time period in the Milankovic calendar
        self.assertEqual(milankovic_count(1696, 1697), 1) #Tests whether there is one leap year btwn 1696 and 1697
        self.assertEqual(milankovic_count(1900, 1901), 0) #Tests whether function outputs 0 leap years in range
        self.assertEqual(milankovic_count(2000, 3000), 243) #Tests no. of leap years over 1000 years
        
#############################################################

if __name__ == "__main__":
    unittest.main() # finds and runs any test methods in our TestCase classes
    main() # needed to actually run the main method
