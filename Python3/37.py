'''
Created on 2018年2月28日

@author: Li
'''
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        return int(str(number)[::-1])
