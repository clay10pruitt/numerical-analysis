"""
:file: bisectionSLM.py

Simple bisection implementation following the algorithm detailed in R.L. Burden,
D.J. Faires, and A.M. Burden Numerical Analysis 10th Ed, Section 2.1.

:author: clayton pruitt
:date: 9/17/2019 (updated with reST documentation style 9/29/2019)
"""

def bisectSLM(f, a, b, TOL, N0):
    """
    Bisection implementation.

    :param f: a function that accepts one numeric parameter
    :param a: the inclusive left-side of the starting interval
    :param b: the inclusive right-side of the starting interval
    :param TOL: the tolerance of accuracy we are looking to be within
    :param N0: the maximum amount of allowed iterations
    :return: some root of the given function within the given accuracy and interval
    """

    # step 1
    i = 1
    FA = f(a)
    # step 2
    while i <= N0:
        # step 3
        p = a + (b - a)/2
        FP = f(p)
        # step 4
        if (FP == 0) or ((b - a)/2 < TOL):
            return p
        # step 5
        i += 1
        # step 6
        if (FA*FP > 0):
            a = p
            FA = FP
        else:
            b = p
    print("Method failed after " + N0 + " iterations.")
    
