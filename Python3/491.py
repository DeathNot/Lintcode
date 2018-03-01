'''
Created on 2018年3月1日

@author: Li
'''
class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        fun = lambda n: int(str(n)[::-1])
        if num == fun(num):
            return True
        else:
            return False
