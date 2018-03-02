'''
Created on 2018年3月2日

@author: Li
'''
class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        # write your code here
        
        a = [i for i in range(100000)]
        for i in range(2, 100000):
            if a[i] != 0:
                try:
                    for j in range(i+i, 100000, a[i]):
                        a[j] = 0
                except:
                    continue
        b = [i for i in a if i > 1]
        for j in range(len(b)):
            if b[j] == n:
                return j + 1
