'''
Created on 2018Äê2ÔÂ27ÈÕ

@author: Li
'''
class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        from functools import reduce
        result = list()
        if len(nums) <= 1:
            return [1]
        for i in range(len(nums)):
            new_nums = nums.copy()
            new_nums.remove(nums[i])
            result.append(reduce((lambda x,y: x*y), new_nums))
        return result
            