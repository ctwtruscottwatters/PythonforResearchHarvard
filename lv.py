# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:57:30 2022

@author: VisualStudio2019
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return 8 * np.abs(x) - np.log2(np.abs(x)) + 8 * np.abs(y) - np.log2(np.abs(y))

def g(x, y):
    return np.abs(np.sin(np.abs(x))) + np.abs(np.cos(np.abs(y)))

def r(x, y):
    return -np.abs(x) + np.abs(x) * np.abs(y)
def main():
    plt.figure(0, dpi=600, figsize=[10, 10])
    x = np.linspace(-2, 2, 16)
    y = np.linspace(-2, 2, 16)
    x, y = np.meshgrid(x, y)
    dy = x - x * y
    dx = x * y - y
    plt.quiver(x, y, dx, dy, color='black', units='xy')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    p = np.linspace(-2, 2, 16)
    q = np.linspace(-2, 2, 16)
    p, q = np.meshgrid(p, q)
    plt.contour(p, q, f(p, q), linewidths=2, cmap='turbo')
    plt.contour(p, q, g(p, q), linewidths=2, cmap='twilight')
    plt.contour(p, q, r(p, q), linewidths=2, cmap='terrain')
    plt.legend(["dy/dx = x - x * y / x * y - y"])
    plt.title("Integral Curve 4 * |x| - ln|x| + 4 * |y| - ln|y|, Integral Curve 0.2 * sin(|x|) + 0.2 * cos(|y|). Implicit Solution - x + x * y")
    plt.xlabel("Charles Truscott Watters. dy/dx v y")
#    plt.show()
    plt.savefig('PredatorPreyEquationsIntegralCurvesNumericalSol2.pdf', dpi=600, papertype='a4', format=None)

if __name__ == "__main__": main()