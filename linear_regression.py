"""
Simple Linear Regression from Scratch using NumPy and Matplotlib

This script demonstrates how to perform simple linear regression on a set of data points 
without using any machine learning libraries. It calculates the regression coefficients 
manually and plots the best-fit line.

Author: Hari Om
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    n = np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x
    return b_0, b_1

def plot_regression_line(x, y, b):
    plt.scatter(x, y, color="g", marker="o", s=30, label="Data points")
    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="b", label="Regression line")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Simple Linear Regression")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {:.2f} \nb_1 = {:.2f}".format(b[0], b[1]))
    print("Number of data points:", np.size(x))
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()
