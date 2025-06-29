import pandas as pd

print(pd.__version__)

series= pd.Series([10,20,30,40,50,60,70,80,90], index=['a','b','c','d','e','f','g','h', 'i'])

print(series)

data = {"Name" : ["Hari", "Ram", "Shyam"], "Age" : [10, 20, 30]}
dataframe = pd.DataFrame(data)
print(dataframe)
#
# csvData = pd.read_csv('data.csv')
#
# print(csvData)
#
# csvData.to_csv("data.csv", index=False)
print("-----------><--------------")

data = {"Name" : ["Hari", "Ram", "Shyam"], "Age" : [10, 20, 30]}
dataframe = pd.DataFrame(data)
print(dataframe.head())

print("-----------><--------------")

print(dataframe.head(1))
print("-----------><--------------")

print(dataframe.tail(2))

print("-----------><--------------")

data = {"Name" : ["Hari", "Ram", "Shyam" , "test1", "test2", "test3"], "Age" : [10, 20, 30, 40, 50, 60]}
dataframe = pd.DataFrame(data)
print(dataframe)
print(dataframe.info())

print("-----------><--------------")

print(dataframe.describe())
print("-----------><--------------")
print(dataframe["Name"])
print(dataframe["Age"])

print("-----------><--------------")
print(dataframe[dataframe["Age"] < 30])

print("-----------><--------------")

print(dataframe.iloc[0])
print("-----------><--------------")

print(dataframe.iloc[:,1])
print(dataframe.iloc[: , 0])



