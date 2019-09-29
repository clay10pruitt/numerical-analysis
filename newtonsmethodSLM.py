"""
:file: newtonsmethodSLM.py

Simple Newton's Method implementation following the algorithm detailed in R.L. Burden,
D.J. Faires, and A.M. Burden Numerical Analysis 10th Ed, Section 2.3.

:author: clayton pruitt
:date: 9/29/2019
"""

def newtonSLM(f, d, p0, TOL, N0):
    """
    Newton's Method implementation.

    :param f: a function that accepts one numeric parameter
    :param d: the first derivative of f
    :param p0: the initial approximation for the root of the function
    :param TOL: the tolerance of accuracy we are looking to be within
    :param N0: the maximum amount of allowed iterations
    :return: an approximation of the root of f
    """

    # step 1
    i = 1
    # step 2
    while i <= N0:
        # step 3
        p = p0 - f(p0)/d(p0)
        # step 4
        if (abs(p - p0) < TOL):
            return p
        # step 5
        p0 = p
        i += 1
    print("Method failed after " + N0 + " iterations.")
