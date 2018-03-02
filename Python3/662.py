'''
Created on 2018年3月2日

@author: Li
'''

"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        max,min = n,1
        mid = int((max + min) / 2)
        while Guess.guess(mid) != 0:
            if Guess.guess(max) == 0:
                return max
            if Guess.guess(min) == 0:
                return min
            if Guess.guess(mid) == 1:
                min = mid - 1
            else:
                max = mid + 1
            mid = int((max + min) / 2)
        return mid
