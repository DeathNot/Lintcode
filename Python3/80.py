'''
Created on 2018年2月28日

@author: Li
'''
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        nums.sort()
        lenth = len(nums)
        if lenth % 2 != 0:
            return nums[ int(lenth / 2)]
        else:
            return nums[int(lenth / 2) - 1] 
        
