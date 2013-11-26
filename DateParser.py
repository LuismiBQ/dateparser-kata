#!/usr/bin/python
# -*- encoding: utf-8 -*-

import itertools
from datetime import datetime

class DateParserException(Exception):
  pass

class DateParser:

  def getPermutations(self, integers):
      permutationsCandidates = itertools.permutations(integers)
      permutationsCandidates = list(permutationsCandidates)

      for i, permutation in enumerate(permutationsCandidates):
        permutationInList = list(permutation)
        if permutationInList[0] < 100: permutationInList[0] += 2000
        permutationsCandidates[i] = permutationInList

      permutationsCandidates.sort()

      return permutationsCandidates

  def getEarlyDate(self, candidates):
      dateConverted = None

      for candidate in candidates:
        try:
          dateConverted = datetime(*candidate)
          if dateConverted.year >= 2000 and dateConverted.year <= 2999:
            break
          else:
            dateConverted = None
        except ValueError:
          pass

      if dateConverted == None:
        raise DateParserException

      return dateConverted

  def parseDate(self, dateString):
    try:
      integers = self.returnIntegers(dateString)
      candidates = self.getPermutations(integers)
      earlyDate = self.getEarlyDate(candidates)

      return str(earlyDate).split()[0]

    except DateParserException:
      return dateString + " is illegal"

  def verifyNoSpaces(self, dateString):
    try:
      dateString.index(' ')
      raise DateParserException
    except ValueError:
      pass

  def splitInFields(self, dateString):
    dateElements = dateString.split('/')

    if len(dateElements) != 3:
      raise DateParserException

    return dateElements

  def convertFieldsToIntegers(self, dateElements):
    dateIntegers = [0, 0, 0]

    try:
      for i, element in enumerate(dateElements):
        dateIntegers[i] = int(element)

    except ValueError:
      raise DateParserException

    return dateIntegers

  def returnIntegers(self, dateString):
    self.verifyNoSpaces(dateString)
    dateElements = self.splitInFields(dateString)
    dateIntegers = self.convertFieldsToIntegers(dateElements)

    return dateIntegers

  def dateInRange(self, dateElements):

    for dateElement in dateElements:
      if dateElement < 0 or dateElement > 2999:
        return False

    return True

  def atMostOneHave4Digits(self, dateElements):
    fourDigitsAlreadyExists = False

    for element in dateElements:
      elementLength = len(element)

      if  elementLength > 2 or elementLength == 0:
        if elementLength == 4 and not fourDigitsAlreadyExists:
          fourDigitsAlreadyExists = True
        else:
          return False

    return True
