'''Write the following methods recursively.

They are mostly exercises that were collected from various sources on
the internet:

  http://academics.tjhsst.edu/compsci/CS2C/U3/recurlab.html
  http://www.cs.arizona.edu/classes/cs227/spring06/misc/24RecursionExercises.htm
  http://www.engr.mun.ca/~theo/Courses/ds/recursion_practice.html
  http://www.cs.arizona.edu/classes/cs227/spring06/misc/50RecursionExercises.htm
'''

def add_commas(n):
    '''Return a string version of integer n with commas added. For example,
    add_commas(15866321) should return "15,866,321".'''
    
    if len(n) <= 3:
        return n
    else:
        return add_commas(n[:-3])+','+ n[-3:]
        

def index(L, v):
    '''Return the index of v in list L.'''
    pass
        

    
def sume(L):
    '''Return the sum of the numbers in list L.'''
    if len(L) == 0:
        return 0
    else:
        return sume(L[:-1]) + L[-1]
    

def _binary_search(L, v, i, j):
    '''Return the index of v in L[i:j], or j if v is not in L.'''
    
    pass
    
def search(L, v):
    return _binary_search(L, v, 0, len(L))

def power(x, n):
    '''Return x to the power n using this formula:

    http://www.enel.ucalgary.ca/People/Norman/engg335_fall1997/recurs/power_t.gif
    '''
    
    pass

def num1s(n):
    '''Write a recursive function that, given a nonnegative int n, yields the
    number of 1's in its binary representation. For example, suppose n = 17.
    The binary representation of 17 is 10001, so the function would return 2.

    The following facts may be useful: 

    (1) The rightmost bit of the binary representation of n is 1 if and only
    if n is odd.

    (2) For n > 0, the binary representation of n is: (binary representation
    of n/2) followed by (the rightmost bit of the binary representation of
    n).'''

    pass

def flatten(L):
    '''Write a recursive function called flatten that takes a list as a
    parameter and flattens it: if any items are themselves lists their
    contents are retrieved from those nested lists.'''
    
    pass
