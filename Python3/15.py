'''
Created on 2018年2月28日

@author: Li
'''
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        import itertools
        result = list()
        for i in itertools.permutations(nums, len(nums)):
            result.append(list(i))
        return result
