import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id =  917079889 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    mean = np.mean(x)
    variance = np.var(x)
    df = len(x) - 1
    critical = norm.ppf((1 + p) / 2, df)
    lower_bound = (df * variance) / critical
    upper_bound = (df * variance) / norm.ppf((1 - p) / 2, df)
    return lower_bound, \
           upper_bound
