'''
Created on 2018年3月1日

@author: Li
'''
class Solution:
    """
    @param str: a string containing uppercase alphabets and integer digits
    @return: the alphabets in the order followed by the sum of digits
    """

    def rearrange(self, strs):
        # Write your code here
        chars = []
        nums = []
        if strs == '':
            return ''
        for i in strs:
            if i.isupper():
                chars.append(i)
            else:
                nums.append(int(i))
        chars.sort()
        return ''.join(chars) + str(sum(nums))
        
