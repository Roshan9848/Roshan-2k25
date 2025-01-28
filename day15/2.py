#label encoder
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "customer_id" : [1,2,3,4,5],
    "ranks": ["good", "average", "bad", "good", "average"],
    "fruits": ["apple", "banana", "orange", "apple", "banana"]
}
df=pd.DataFrame(data)
print("original data")
print(df)

#apply the label encoder to ranks and fruits
encoder = LabelEncoder()
df["ranks_encoded"] = encoder.fit_transform(df["ranks"])
df["fruits_encoded"] = encoder.fit_transform(df["fruits"])
print("/nlabel encoded data")
print(df)