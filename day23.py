import pandas as pd
import numpy as np

data = {
    "Name": ["Akshmith", "Roopesh", "Pranvi", "Karan", "Suraksha"],
    "Machine Learning": [85, np.nan, 92, 74, 88],
    "Python": [90, 82, 89, np.nan, 91],
    "Java": [np.nan, 76, 95, 72, 84],
    "DBMS": [np.nan, 90, 69, 70, np.nan]
}

df = pd.DataFrame(data)

print("Original DataFrame:\n")
print(df)

print("\nMissing Values:\n")
print(df.isnull())

df.fillna(df.mean(numeric_only=True), inplace=True)
print("\nDataFrame after filling missing values:\n")
print(df)

df["Total"] = df[["Machine Learning", "Python", "Java", "DBMS"]].sum(axis=1)
print("\nUpdated DataFrame with Total:\n")
print(df)
