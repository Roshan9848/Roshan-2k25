import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)
data = {
    "study Hours": np.random.randint(1,10,50),
    "Marks": np.random.randint(30,100,50),
    "screen Time": np.random.randint(1,7,50),
    "Traveling Time": np.random.randint(0,3,50),
    "sleep Hours": np.random.randint(4,10,50),
}
df = pd.DataFrame(data)
corr = df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr,annot=True, cmap="coolwarm", fmt=".2f",linewidths=0.5)
plt.title("Feature Correlation Heatmap ")
plt.show()
