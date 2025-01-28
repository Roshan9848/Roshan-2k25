    import pandas as pd
from sklearn.preprocessing import OneHotEncoder

#sample dataset
data = {
    "customer_id": [1, 2, 3, 4, 5],
    "gender": ["male", "female", "male", "female", "male"],
    "country": ["USA", "Canada", "USA", "Canada", "UK"],
    "fruits": ["apple", "banana", "orange", "apple", "banana"]
}
df = pd.DataFrame(data)
print("original data")
print(df)

#apply onehotencoder
encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(df[["gender", "country","fruits"]])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(["gender", "country","fruits"]))
df = pd.concat([df, encoded_df], axis=1)
df.drop(["gender", "country","fruits"], axis=1, inplace=True)
print("/nencoded data")
print(df)