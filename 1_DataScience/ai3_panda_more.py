import pandas as pd

csv_data = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/iris.csv")
print(csv_data)
print("-----------><--------------")
print(csv_data.shape)

print(csv_data.head())
print(csv_data.describe())

print("-----------><--------------")

sepalLength = csv_data["SepalLength"]
print(sepalLength)
print("-----------><--------------")

filterdColumns = csv_data[["PetalLength", "Name"]]
print(filterdColumns)

filterdRows = csv_data[(csv_data["PetalWidth"] == 0.2) & (csv_data["SepalLength"] > 5)]
print(filterdRows)