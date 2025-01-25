=import statistics 
import numpy as np
stock_prices = [100,102,98,105,101,97,99,103,100,98]

variance = statistics.variance(stock_prices)
print(f"Variance of stock prices: {variance}")

numpy_variance = np.var(stock_prices,ddof=1)
print(f"Variance of stock prices (using NumPy): {numpy_variance}")


#2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {.
        'Temperature':[22,25,20,18,21,19],
        'Humidity':[65,60,72,78,70,75],
        'Wind speed':[15,10,20,25,12,14]
        'pressure':[10,15,28,27,29]
        }

        df = pd.DataFrame(data)
        #pendingg...