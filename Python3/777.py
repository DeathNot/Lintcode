'''
Created on 2018年3月2日

@author: Li
'''
class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        # write your code here
        for i in range(num+1):
            if num > i**2:
                continue
            elif num == i**2:
                return True
            else:
                return False
