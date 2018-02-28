'''
Created on 2018年2月28日

@author: Li
'''
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        result = ""
        for i in s.split(' ')[::-1]:
            result = result + i + ' '
        return result.strip()
