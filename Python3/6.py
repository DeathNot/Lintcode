'''
Created on 2018Äê2ÔÂ27ÈÕ

@author: Li
'''
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        import itertools
        A = list(itertools.chain.from_iterable([A, B]))
        A.sort()
        return A