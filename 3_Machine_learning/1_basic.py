
import pandas as pd
from sklearn.model_selection import train_test_split

import seaborn as sns
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv"
df = pd.read_csv(url)

print(df.head())
feature = df[['total_bill', 'size']]
target = df['tip']

print("Feature \n ", feature.head())
print("Target: \n ", target.head())

X_train, X_test, Y_train, Y_test = train_test_split(feature, target, test_size=0.2, random_state=42)
print("X_train \n ", X_train.shape)
print("X_test \n ", X_test.shape)
print("Y_train \n ", Y_train.shape)
print("Y_test \n ", Y_test.shape)


#plotting
sns.pairplot(df, x_vars=['total_bill', 'size'], y_vars=['tip'], height=5, aspect=0.8, kind="scatter")
plt.title("Features  vs target")
plt.show()