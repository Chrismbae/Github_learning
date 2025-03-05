import numpy as np
import matplotlib.pyplot as plt  # Fixed typo in import

def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)

def calculate_variance(data):
    if not data:
        return 0
    mean = calculate_mean(data)  # Fixed typo: 'meaq' -> 'mean'
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_standard_deviation(data):
    import math
    return math.sqrt(calculate_variance(data))

def calculate_median(data):
    if not data:
        return 0
    data.sort()
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]
