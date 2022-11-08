#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 00:39:35 2022

@author: Charles Thomas Wallace Truscott

Byron Bay NSW 2481

127 Broken Head Rd, Suffolk Park NSW 2481

Massachusetts Institute of Technology, Harvard via edX student

Fine for permutations of the first odd number, 3, and fine for permutations of the second even number, 4

Need to prove theorem for all permutation sizes of even, odd and prime numbers (quick arithmetic in head presumed a conjecture is that one less than each prime number is an even number). Guessing factors of a number are the indices..

One quick conjecture is that the inner loop is n!/n times executed once each has taken the place of the subscript up to `n` times and switched with the subscript 0

Thank you Massachusetts Institute of Technology, need to prove this for all even, odd and prime factorial input, perhaps recursively proving the base cases for 0, 1, 2, using the algorithm for 3 and 4, and splitting all factors of subsequent numbers into a combinatorial definition of blocks of 3 and for (e.g. for nine the permutation applied 3 times for 3 blocks of 3 in definition, for 11 the permutation algorithm applied in a single block of one for 5 permutation boxes of 2)

runfile('/home/alienware/Desktop/permutations_alg_complex.py', wdir='/home/alienware/Desktop')
['D', 'B', 'C', 'A']
['B', 'D', 'C', 'A']
['B', 'C', 'D', 'A']
['A', 'C', 'D', 'B']
['C', 'A', 'D', 'B']
['C', 'D', 'A', 'B']
['D', 'A', 'C', 'B']
['A', 'D', 'C', 'B']
['A', 'C', 'D', 'B']
['B', 'C', 'D', 'A']
['C', 'B', 'D', 'A']
['C', 'D', 'B', 'A']
['D', 'B', 'A', 'C']
['B', 'D', 'A', 'C']
['B', 'A', 'D', 'C']
['C', 'A', 'D', 'B']
['A', 'C', 'D', 'B']
['A', 'D', 'C', 'B']
['A', 'B', 'C', 'D']
['B', 'A', 'C', 'D']
['B', 'C', 'A', 'D']
['D', 'C', 'A', 'B']
['C', 'D', 'A', 'B']
['C', 'A', 'D', 'B']
24

runfile('/home/alienware/Desktop/permutations_alg_complex.py', wdir='/home/alienware/Desktop')
['C', 'B', 'A']
['B', 'C', 'A']
['C', 'A', 'B']
['A', 'C', 'B']
['A', 'B', 'C']
['B', 'A', 'C']
6

"""

def factorial(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        y = 2
        for x in range(3, n + 1):
            y *= x
        return int(y)
    
def permutation(R):
    f = factorial(len(R))
    f_l = len(R) - 1
    f_r = factorial(len(R) - 1)
    f_rc = factorial(len(R) - 1)
    count = 0
    for x in range(0, len(R), 1):
        L = R.copy()
        temp = L[x]
        oth = L[0]
        L[0] = temp
        L[x] = oth

#        print(L)
        while(f_r > 0):
            for z in range(0, len(R) - 1, 1):
#                print(z % len(R) - 1)
                ss = z % len(R) - 1
                l = L[ss]
                r = L[z]
                L[ss] = r
                L[z] = l
                print(L)
                count += 1
            f_l = len(L) - 1
            f_r -= len(R) - 1
        f_r = factorial(len(R) - 1)
    print(count)
    return 0

def main():
#    permutation(['A', 'B', 'C'])
    String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    L = []
    R = []
    p = 0
    permutation(['A', 'B', 'C'])
#    for x in range(2, 9, 2):
#        print(String[0:x + 1])
#        for y in String[0:x + 1]:
#            L.append(y)
#        R.append(L)
#        L = []
#    for z in range(0, int(len(R)), 1):
#        permutation(R[z])
#    permutation(['A', 'B', 'C', 'D', 'E'])
#    permutation(['A', 'B', 'C', 'D', 'E', 'F'])
#    permutation(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
#    f.close()
if __name__ == "__main__": main()