'''
Created on 2018年3月2日

@author: Li
'''
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        def cmp(a):
            return -1 if a % 2 != 0 else 1
        
        nums.sort(key = cmp)