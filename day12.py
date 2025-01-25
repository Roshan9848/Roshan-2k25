import pandas as pd 
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns
np.random.seed(10)
data = pd.DataFrame({
    'value:np.concatenate([np.random.normal(10,1,10)])'
})
Q1 = data['value'].quantile(0.25)
Q2 = data['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper-bound = Q3 - 1.5 * IQR
outliers = data[data['value'] < lower bound) | (data['value'] > upper_bound)
print(f"outliers based on Box Plot criteria:\n{outliers}")
plt.figure(figsize=(12,6))
plt.subplot(1,2,3)
sns.boxplot(x=data['value'])
plt.title('Box Plot')