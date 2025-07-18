import pandas as pd
from  sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf


# Load data
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"
data = pd.read_csv(url)

print(data)

#Feature

# Simple feature selection
features = ['Pclass', 'Sex', 'Age', 'Fare']
data = data[features + ['Survived']].dropna()

le = LabelEncoder()
data['Sex'] = le.fit_transform(data['Sex'])

X = data[features]
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(4, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


#compile model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Fit model
model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test))

model.save("titanic_model.h5")

