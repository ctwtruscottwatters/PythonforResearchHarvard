import math
import numpy
from matplotlib import pyplot as plot
import os
# Charles Truscott
# Massachusetts Institute of Technology
# August 17, 2022, 4:02 p.m.
# All my own work
# Number system logic in Python, seems to defy integer and float wrapping
# I love you Dad Mark William Watters, big bro Tai William Wedekind Truscott


class ArithmeticalOperation(object):
    def __init__(self, p, q, r=0, s=0):
        self.p = p
        self.q = q
        self.r = r
        self.s = s
    def __str__(self):
        return str("<{}, {}>, <{}, {}>".format(p, q, r, s))
    def add(self):
        addend_one = 0
        addend_two = 0
        for x in range(self.p):
            addend_one += 1
        for y in range(self.q):
            addend_two += 1
        for z in range(addend_two):
            addend_one += 1
        return addend_one
    def subtract(self):
        subtrahend_one = 0
        subtrahend_two = 0
        for x in range(self.p):
            subtrahend_one += 1
        for y in range(self.q):
            subtrahend_two += 1
        for z in range(subtrahend_two):
            subtrahend_one -= 1
        return subtrahend_one
    def multiply(self):
        multiplicand = 0
        for x in range(1, 1 + self.q):
            multiplicand += self.p
        return multiplicand
    def divide(self):
        dividend = float(0.0)
        remainder = 0
        number_to_divide = self.p
        number_to_divide_by = self.q
        epsilon = 0.000001
        while(number_to_divide >= number_to_divide_by):
            number_to_divide -= number_to_divide_by
            dividend += 1
        print(number_to_divide)
        L = []
        step = 0.0000001
#        while(number_to_divide >= epsilon):
#            number_to_divide -= step * number_to_divide_by
#            dividend += step
        remainder = float(number_to_divide)
        high = remainder
        low = 0
        guess = (high + low) / 2.0
        while(round(abs((remainder - (((( round(abs(float(guess)) , 12)) * number_to_divide_by))))), 7) >= step):
#           print("guess: {} dividend: {}".format(guess, dividend + guess))
            if (remainder < ((round(abs(float(guess)) , 12)) * number_to_divide_by )):
                high = guess
            elif (remainder > ((round(abs(float(guess)) , 12)) * number_to_divide_by )):
                low = guess
            guess = (high + low) / 2.0
            
        dividend += guess
#        while(x < 100000):
#            dividend += (1/x) * (number_to_divide % (1/x * number_to_divide_by))
#            number_to_divide -=  (1/x) * #(number_to_divide % (1/x * number_to_divide_by))
#           print(number_to_divide)
#            x += 10 * x
           
        # Yay. All my own work. Approximate answer for solving remainder division all my own work by Charles Truscott Watters. I love MIT. Massachusetts Institute of Technology
#       while(x <= number_to_divide):
#            dividend += number_to_divide_by * 1/#10000000
#            x += number_to_divide_by * 1/10000000
        # Exhaustive Enumeration
        return round(dividend, 6)
    def exponentiate(self, exponent):
        base = self.p
        exponent = exponent
        power = 1
        for x in range(1, 1 + exponent, 1):
            power *= base
        return power
        
class DecimalFraction(ArithmeticalOperation):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    pass
    
def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    birthdays = ArithmeticalOperation(x, y)
    print("{} + {} = {}".format(birthdays.p, birthdays.q, birthdays.add()))
    print("{} - {} = {}".format(birthdays.p, birthdays.q, birthdays.subtract()))
    print("{} * {} = {}".format(birthdays.p, birthdays.q, birthdays.multiply()))
    print("{} / {} = {}".format(birthdays.p, birthdays.q, birthdays.divide()))
    print("{} to the power of {} = {}".format(birthdays.p, birthdays.q, birthdays.exponentiate(birthdays.q)))
    
    
    
if __name__ == "__main__": main()