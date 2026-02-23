import math
import time
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

n = 1000000
N1 = np.sort(np.random.randint(0, n**2, n))
N2 = np.sort(np.random.randint(0, n**2, n))[::-1]
N3 = np.random.randint(0, n**2, n)
N4 = np.random.randint(0, n**2, n)
N5 = np.random.randint(0, n**2, n)
N6 = np.random.uniform(0, n**2, n)
N7 = np.random.uniform(0, n**2, n)
N8 = np.random.uniform(0, n**2, n)
N9 = np.random.uniform(0, n**2, n)
N10 = np.random.uniform(0, n**2, n)

data_set = [N1, N2, N3, N4, N5, N6, N7, N8, N9, N10]