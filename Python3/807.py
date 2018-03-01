'''
Created on 2018年3月1日

@author: Li
'''
class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        snum = bin(n)[2:]
        if (snum == snum[::-1]):
            return True
        else:
            return False
