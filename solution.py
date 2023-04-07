import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
	q = 1 - p
	loc = x.mean()
	n = len(x)
	sum_variance = np.sum((x - loc)**2) / n
	lower_bound_chi2 = chi2.ppf(q / 2, n)
	upper_bound_chi2 = chi2.ppf(1 - q / 2, n)

	# Доверительный интервал для дисперсии
	lower_bound_variance = n * sum_variance / upper_bound_chi2
	upper_bound_variance = n * sum_variance / lower_bound_chi2

	lower_ans = np.sqrt(lower_bound_variance / 18)
	upper_ans = np.sqrt(upper_bound_variance / 18)
	return lower_ans, upper_ans
