'''
Created on 2018年3月1日

@author: Li
'''
class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        # write your code here
        if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
            return True
        else:
            return False
