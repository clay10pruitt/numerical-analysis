"""
:file: fixedpointiterationSLM.py

Simple fixed-point iteration implementation following the algorithm detailed in R.L. Burden,
D.J. Faires, and A.M. Burden Numerical Analysis 10th Ed, Section 2.2.

:author: clayton pruitt
:date: 9/29/2019
"""

def fpiSLM(g, p0, TOL, N0):
    """
    Fixed-point iteration implementation.

    :param g: a function that accepts one numeric parameter
    :param p0: the initial approximation for p
    :param TOL: the tolerance of accuracy we are looking to be within
    :param N0: the maximum amount of allowed iterations
    :return: an approximation to the solution p = g(p)
    """

    # step 1
    i = 1
    # step 2
    while i <= N0:
        # step 3
        p = g(p0)
        print("p: " + str(p))
        # step 4
        if (abs(p - p0) < TOL):
            return p
        # step 5
        p0 = p
        i += 1
    print("Method failed after " + N0 + " iterations.")
