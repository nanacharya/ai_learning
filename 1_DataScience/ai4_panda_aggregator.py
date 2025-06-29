import pandas as pd
import numpy as np

data = {
    "Class": ["class 1", "class 2", "class 1", "class 4", "class 3", "class 1", "class 2"],
    "Score": [22, 33, 34, 35, 36, 37, 38],
    "Age": [10, 20, 10, 40, 50, 40, 50],

}

print(data)

print("-----------><--------------")

df = pd.DataFrame(data)
print(df)

print("-----------><--------------")

groupedByClass = df.groupby('Class').mean()
print(groupedByClass)

print("-----------><--------------")
# groupedByAge = df.groupby('Age').mean()
# print(groupedByAge)

aggregatorData = df.groupby('Class').agg(
    {'Age': ["mean", "median", "max", "min"]}
)
print(aggregatorData)

aggregatorData = df.groupby('Class').agg(
    {'Age': ["mean", "median", "max", "min"],
    'Score': ["mean", "median", "max", "min"]}
)

print(aggregatorData)