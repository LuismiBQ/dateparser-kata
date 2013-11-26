#!/usr/bin/python
# -*- encoding: utf-8 -*-

import unittest
from DateParser import DateParser, DateParserException
from itertools import izip

class DateParserTest(unittest.TestCase):

  def setUp(self):
    self.date = DateParser()

  # The input file consists of a single line containing three integers
  # separated by "/". There are no extra spaces around the "/" ...

  def test_stringWith3Integers(self):

    dateString = "12/17/85"
    self.assertEqual(self.date.returnIntegers(dateString), [12, 17, 85])

  def test_badStrings(self):
    dateStrings = ["sdklafj/12/97", "12/23/23/19", "12 /37/99"]

    for dateString in dateStrings:
      with self.assertRaises(DateParserException):
        self.date.returnIntegers(dateString)

  # ...between 0 and 2999, ... 

  def test_dateInRange(self):
    dates = [[12, 34, 2011], [23,67,199], [1,1,2]]

    for date in dates:
      self.assertTrue(self.date.dateInRange(date))

  def test_dateNotInRange(self):
    dates = [[12, 34, 3111], [-3,67,199], [1,1000000000,2]]

    for date in dates:
      self.assertFalse(self.date.dateInRange(date))

  # At most one of the integers has four digits, and the others have one or two
  # digits.
  
  def test_validSizes(self):
    dates = [["3", "32", "8887"], ["31", "3486", "98"], ["98", "1", "2"]]

    for date in dates:
      self.assertTrue(self.date.atMostOneHave4Digits(date))
  
  def test_invalidSizes(self):
    dates = [["3", "832", "8887"], ["831", "3486", "98"], ["88898", "1", "2"], ["8898", "1", ""]]

    for date in dates:
      self.assertFalse(self.date.atMostOneHave4Digits(date))
  
  def test_atMostOneHave4Digits(self):
    dates = [["23", "32", "87"], ["31", "3486", "98"]]

    for date in dates:
      self.assertTrue(self.date.atMostOneHave4Digits(date))

  def test_moreThanOneHave4Digits(self):
    dates = [["23", "2232", "2287"], ["1131", "3486", "98"], ["1131", "3486", "8998"]]

    for date in dates:
      self.assertFalse(self.date.atMostOneHave4Digits(date))

  def test_getEarlyDate(self):
    dates = ["02/4/67", "31/9/73", "2014/2/29"]
    results = ["2067-02-04", "31/9/73 is illegal", "2014/2/29 is illegal"]

    for date, result in izip(dates, results):
      self.assertEqual(self.date.parseDate(date), result)

if __name__ == "__main__":
  unittest.main()
