# chatbot_server.py
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("titanic_model.h5")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    try:
        pclass = int(data.get("pclass"))
        sex = 1 if data.get("sex") == "male" else 0
        age = float(data.get("age"))
        fare = float(data.get("fare"))

        input_data = np.array([[pclass, sex, age, fare]])
        prediction = model.predict(input_data)[0][0]

        response = f"I predict a survival probability of {prediction:.2f}"
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
