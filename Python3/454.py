'''
Created on 2018��2��27��

@author: Li
'''
class Rectangle:

    '''
     * Define a constructor which expects two parameters width and height here.
    '''
    # write your code here
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    '''
     * Define a public method `getArea` which can calculate the area of the
     * rectangle and return.
    '''
    # write your code here
    def getArea(self):
        return self.height * self.width
