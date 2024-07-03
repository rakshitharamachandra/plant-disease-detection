from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd
import predictedmodel as mymodel
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)


UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/another')
def another():
    return render_template('another.html')

@app.route('/predictor')
def predictor():
    return render_template('classify.html')


@app.route('/predict', methods=['POST'])
def predict():
    
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']

    
    if file.filename == '':
        return jsonify({"error": "No selected file"})
    
    print("Predicting on a normal plant :")

    if file:
       
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        filepath = "upload/"+filename
        print("file path:", filepath)

        
        prediction = mymodel.predict_class(filepath)

        return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)
