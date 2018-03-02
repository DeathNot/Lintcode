'''
Created on 2018年3月2日

@author: Li
'''
class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        count = len(nums) - 1
        for i in range(int(len(nums) / 2)):
            nums[i] += nums[count -i]
            nums[len(nums) - 1 - i] = nums[i] -  nums[count -i]
            nums[i] = nums[i] - nums[count -i]
