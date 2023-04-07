import pandas as pd
import numpy as np
import scipy.stats as norm

chat_id = 917079889 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    x_bar = np.mean(x)
    s = np.std(x)
    chi_sq_left = norm.chi2.ppf((1 - p/2), df=n-1)
    chi_sq_right = norm.chi2.ppf(p/2, df=n-1)
    left = np.sqrt((n-1)*s**2/chi_sq_left)
    right = np.sqrt((n-1)*s**2/chi_sq_right)
    return (x_bar - left, x_bar + right)
