'''
Created on 2018年2月28日

@author: Li
'''
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        import itertools
        result = list()
        for i in itertools.permutations(nums, len(nums)):
            result.append(i)
        return [list(i) for i in set(result)]