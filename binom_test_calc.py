import numpy as np

from scipy.stats import binom_test
import matplotlib.pyplot as plt


def binom_calc(k, p=0.5, alternative='greater', plot=False):
    """Function to calculate binom test over a range to find threshold

    Parameters
    ----------
    k : int
    p : float
    alternative : str

    Returns
    -------

    """
    results = np.zeros(k)  # results vector

    # loop to calculate binom_test results
    for ii in range(k):
        results[ii] = binom_test(k - ii, k, p=p, alternative=alternative)

    # Find the threshold for significant
    threshold = len(results[results <= 0.05]) - 1
    p_val = results[threshold]
    successes_needed = k - threshold
    percent = successes_needed / k

    if plot:
        plt.figure()
        plt.plot(np.arange(k) + 1, results[::-1])
        plt.gca().invert_xaxis()  # revert x-axis
        plt.hlines(0.05, k + 1, 1)
        plt.grid()
        plt.show()

    return threshold, p_val, successes_needed, percent
