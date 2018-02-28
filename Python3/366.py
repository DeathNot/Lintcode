'''
Created on 2018Äê2ÔÂ27ÈÕ

@author: Li
'''

class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        i,x,y = 0,0,1
        for i in range(n-1):
            x,y = y,x+y
        return x
