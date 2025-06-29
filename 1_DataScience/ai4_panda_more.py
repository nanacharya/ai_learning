import pandas as pd
import numpy as np

data = {

    "name": ["Ram", "Shyam", "Hari", np.nan, "Sita"],
    "salary": [np.nan, 200, 300, 400, 500],
    "age": [10, 20, 30, 40, np.nan],

}

data1= {
    "name": ["Ram", "Shyam", "Hari", np.nan, "Sita"],
    "address":["address1","address2","address3","address1","address2"],
    "city":["city1","city2","city3","city1", "city5"],

}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
print(df)

print("-----------><--------------")
df["salary"] = df["salary"].fillna(df["salary"].mean())
print(df)

print("-----------><---------------")

df["age"] = df["age"].interpolate()
print(df)

print("-----------><---------------")

df = df.rename(columns={"salary": "Monthly Salary"})
print(df)


print("-----------><---------------")

merged_data = pd.merge(df, df1, how="inner")
print(merged_data)