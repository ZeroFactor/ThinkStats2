"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def PmfMean(pmf):
    """Returns the mean of the pmf.

    pmf: Pmf object

    returns: mean from pmf
    """
    resultMean = 0

    for val, freq in pmf.Items():
        resultMean += val * freq

    return resultMean


def PmfVar(pmf):
    """Returns the variance of the pmf.

    pmf: Pmf object

    returns: variance of the pmf
    """
    mean = PmfMean(pmf)
    resultVar = 0

    for val, freq in pmf.Items():
        resultVar += freq * pow((val - mean), 2)

    return resultVar


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    pmf = thinkstats2.Pmf(live.prglngth)

    # test Mode
    mean = PmfMean(pmf)
    print('Mean of preg length', mean)
    assert mean == pmf.Mean(), mean

    variance = PmfVar(pmf)
    print('Variance of preg length', variance)
    assert variance == pmf.Var(), variance

    # test AllModes
    # modes = AllModes(hist)
    # assert modes[0][1] == 4693, modes[0][1]

    # for value, freq in modes[:5]:
    # print(value, freq)

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
