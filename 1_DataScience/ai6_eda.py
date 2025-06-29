import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Exploratory Data Analysis


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
data = pd.read_csv(url)
print(data.info())
print(data.describe())

print(data.head(10))
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

print(data.info())

data = data.drop_duplicates()
print(data.info())

firstClassPassenger = data[data["Pclass"] == 1]

print(firstClassPassenger)


#Survival rate by class

# survivalGroup = data.groupby("Pclass")["Survived"].mean()
# survivalGroup.plot(kind='bar', color='skyblue')
# plt.title("Survival Distribution")
# plt.ylabel("Percentage of Survived")
# plt.show()


# Histogram : age distribution

sns.histplot(data["Age"], kde= True, bins=20, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

