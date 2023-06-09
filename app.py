import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=["POST", "GET"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = prediction

    return render_template("result.html", result=output)


@app.route('/predict_api', methods=["POST"])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
