'''
Created on 2018年2月28日

@author: Li
'''
class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        # write your code here
        fun = lambda x: int(str(x)[::-1])
        if n >= 0:
            n = fun(n)
        else:
            n = -1 * fun(-1 * n)
        result = n if n < 2147483647 else 0
        return result
            
