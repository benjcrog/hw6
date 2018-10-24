#       cd ~/desktop/project1/hw6
#       python hw6.py

import re
import unittest

def sumNums(fileName):
    count = 0
    numbers = []
    f = open(fileName)
    for i in f:
        numList = re.findall('[0-9]+',i)
        numbers = numbers + numList
    print(numbers)
    for i in numbers:
        count = count + int(i)
    return count

    


def countWord(fileName, word):
    wordList = []
    lenOfList = 0
   
    f = open(fileName)
    for line in f:
       #re.findall(r'\b' + word + r'b')
        wordAt = re.findall(r'\b' + word + r'\b', line, flags = re.IGNORECASE)
        
        wordList = wordList + wordAt
    lenOfList = len(wordList)
    return(lenOfList)

#
# def listURLs(fileName):
#     pass


#print(sumNums("regex_sum_42.txt"))
print(countWord("regex_sum_42.txt", "computer"))


# class TestHW6(unittest.TestCase):
#     """ Class to test this homework """
#
#     def test_sumNums1(self):
#         """ test sumNums on the first file """
#         self.assertEqual(sumNums("regex_sum_42.txt"), 445833)
#
#     def test_sumNums2(self):
#         """ test sumNums on the second file """
#         self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)
#
#     def test_countWord(self):
#         """ test count word on the first file """
#         self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)
#
#     def test_listURLs(self):
#         """ test list URLs on the first file """
#         self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)
#
# # run the tests
# unittest.main(verbosity=2)
