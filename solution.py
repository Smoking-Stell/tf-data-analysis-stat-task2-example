import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
	q = 1 - p
	loc = np.mean(x**2)

	n = len(x)
	sigma_mle = loc / np.sqrt(np.pi / 2)

	lower_bound_chi2 = chi2.ppf(q / 2, n - 1)
	upper_bound_chi2 = chi2.ppf(1 - q / 2, n - 1)

	lower_bound_sigma = (n - 1) * sigma_mle**2 / upper_bound_chi2
	upper_bound_sigma = (n - 1) * sigma_mle**2 / lower_bound_chi2

	lower_ans = np.sqrt(lower_bound_sigma / 18)
	upper_ans = np.sqrt(upper_bound_sigma / 18)
	return lower_ans, upper_ans
