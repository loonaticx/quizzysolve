"""
Quizzy Solver

Original Author: Chidambaram Annamalai (quantumelixir)
Date: 01/15/2011
https://gist.github.com/quantumelixir/780823

Modified by Loonatic to support Python 3 and Windows

Resources Used:
https://github.com/dwyl/english-words/blob/master/words_dictionary.json

Usage:
python quizzy.py words.txt
(see example input on the bottom)

"""

# 1. The input is a list of rings. Each ring is a list of letters.
# 2. Once you choose a letter from ring k then you can only choose letters from
#   ring k, k + 1, ... Outermost ring is ring 0. And ring depth increases inwards.
# 3. points[k] is the points for getting the letter chr(k + ord('A'))

from bisect import bisect, bisect_left
import json
from time import time


class Solver(object):

    def __init__(self, ringfile, points=[1] * 26, dictionary='words_dictionary.json', minlen = 3, maxlen=15):
        """
        Setup the base. Use default scrabble scoring when points is unspecified.

        :param ringfile: File that includes entries of rings. Each ring is a list of letters.
        :param points: points[k] is the points for getting the letter chr(k + ord('A'))
        :param dictionary: JSON file of words to reference.
        :param minlen: Minimum character length for output. Use this to adjust threshold.
        :param maxlen: Maximum character length for output. Use this to adjust threshold.
        """
        dictionary = json.load(open(dictionary))

        self.words = [i[:-1].upper() for i in dictionary if i[:-1].isalpha()]
        self.words.sort()  # just in case
        self.points = points
        self.parse(ringfile)

        self.depth = len(self.rings)
        self.possibilities = []
        self.tried = set()
        self.minlength = 3
        self.maxlength = maxlen

    def parse(self, ringfile):
        rings = []
        for line in open(ringfile):
            if line.strip():
                rings += [list(line.strip().upper())]
        self.rings = [[[j, True] for j in i] for i in rings]

    def isvalid(self, word):
        """
        Check the validity of the word using binary search
        """
        index = bisect(self.words, word)
        dictword = self.words[index - 1]
        # print("DICTWORD = " + dictword)
        # print("WORD = " + word)
        if index == 0 or dictword != word:
            # print("FAIL")
            return False
        # print("PASS")
        return True

    def wordworth(self, word):
        """
        :return the points scored for the input word.
        """
        ret = 0
        for letter in word:
            ret += self.points[ord(letter) - ord('A')]
        return ret

    def nowordwithstart(self, start):
        """
        :return: True if there is no word that begins with the input.
        """
        index = bisect_left(self.words, start)
        try:
            if self.words[index].startswith(start):
                return False
        except IndexError:
            return True
        return True

    def suggest(self, tillnow='', curDepth=0):
        """
        Recursive Depth First Search. Adds valid words to self.possibilities
        """
        # not interested
        if len(tillnow) > self.maxlength or self.nowordwithstart(tillnow) or tillnow in self.tried:
            return False

        # memoize : add to the list of tried ends
        self.tried.update([tillnow])

        # if its a word then add to the list of possibilities
        if len(tillnow) >= self.minlength and self.isvalid(tillnow):
            self.possibilities += [(self.wordworth(tillnow), tillnow)]

        # pick more letters from this ring or a deeper ring
        for i in range(curDepth, self.depth):
            # in this depth pick a (letter, availability) pair
            for pair in self.rings[i]:
                # if the letter is available
                if pair[1]:
                    pair[1] = False
                    # recurse : find words with this as a beginning
                    self.suggest(tillnow + pair[0], i)
                    pair[1] = True

    def solve(self):
        # t = time()
        self.suggest()
        self.possibilities.sort(key=lambda x: x[0], reverse=True)
        for worth, word in self.possibilities:
            pass
            print(word)


# print 'Took %.3f seconds' % (time() - t)

if __name__ == '__main__':
    import os
    import sys

    inputfile = 'ringfile.txt'

    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        inst = Solver(sys.argv[1])
        inst.solve()
    elif os.path.isfile(inputfile):
        inst = Solver(inputfile, maxlen=8)
        inst.solve()
    else:
        # todo: We can't find the input file they gave us, so let's just use good ol' traditional input()
        print('Did you give the right filename?')

"""
Example Data

Outermost Ring
----
A B C D
B     C
C     B
D C B A

Input:
ABCDBCDCBABC

Inner Ring
---
A B C
B   B
C B A

Input:
ABCBABCB

Innermost Ring
A

Input:
A

Example Input file:
endeoatifldiolrt
aolcetee
t
"""
