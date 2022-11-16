#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:16:55 2022

@author: truscottwatters
"""

import pandas as pd
import numpy as np
import scipy.stats as ss

# Still learning Pandas, scikitlearn and matplotlib and scipy and numpy
# Need numerical coefficient formulas
# Upset I'm struggling with a basic problem of cost-per-unit in code
# would use import decimal but still getting to know the standard library
# need to, yeah, learn conditional definition of pandas columns and rows
# trying
def main():
    A = ["Waterproof Matches", "Firelighters", "Alcohol Wipes", "Disinfectant Wipes", "Soap", "Masks", "Hand Sanitiser in mL", "Picnic Basket"]
    B = [21, 17.50, 100, 99.95, 50, 14, 65, 120]
    C = [2 * 160, 100, 500, 225, 20, 50, 30 * 500, 1]
    cd = pd.DataFrame({"Item": A, "Cost": B, "Amount": C})
#    for value in cd["Cost per unit"]:
#        for power in enumerate(0, 1, 2, 3):
#            if value % (10 ** power) == 0:
    L = []
    R = []
    Q = []
    S = []
    for value in cd["Cost"]:
        if value / 10 ** 1 < 0:
            L.append("Dollars")
            R.append(1)
        elif ((value / 10 ** 1) > 0) and ((value / 10 ** 1) < 10):
            L.append("Tens")
            R.append(10)
        elif (value / 10 ** 2) < 10 and ((value / 10 ** 2) > 0):
            L.append("Hundreds")
            R.append(100)
#        elif value / 10 ** 3 < 0:
#            L.append("Thousands")
    for amount in cd["Amount"]:
        if amount == 1:
            Q.append("Minus order of cost")
            S.append(0)
        elif amount / 10 ** 1 < 0:
            Q.append("Ones")
            S.append(1)
        elif ((amount / 10 ** 1) > 0) and ((amount / 10 ** 1) < 10):
            Q.append("Tens")
            S.append(10)
        elif (amount / 10 ** 2) < 10 and ((amount / 10 ** 2) > 0):
            Q.append("Hundreds")
            S.append(100)
        else:
            Q.append("NULL")
            S.append(0)
    cd["Dollar Range"] = L
    cd["Numerical Dollar Range"] = R
    cd["Amount Range"] = Q
    cd["Numerical Amount Range"] = S
    cd["Cost per unit"] = cd["Cost"] / cd["Amount"] # * cd["Numerical Dollar Range"]  / cd["Numerical Amount Range"] * 10
#    cd["Cost per unit"] = cd["Cost per unit"]
    print(cd.head())
#    A = []
#    for x in range(0, len(R), 1):
#        if R[x] > S[x]:
#        elif R[x] < S[x]:
#    cd["Cost per unit"] = (cd["Cost"].values / cd["Amount"].values) * cd["Numerical Amount Range"] / cd["Numerical Dollar Range"]
    cd.to_csv('./DisasterMgmtCharlesTruscott.csv')
#    cd["Cost Per Unit"] = 
#    cd.to_csv('./test1.csv')
#    cd = cd.drop(columns=["Cost per unit"])
#    print(cd)
if __name__ == "__main__": main()