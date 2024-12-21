from flask import Flask, render_template, request,jsonify
from src.ImageProcessors.ProcessImage import process_image_func
from src.ImageProcessors.ImageIO import ImageOI
from src.ImageProcessors.functions import *
import os

app = Flask(__name__)
from random import randint
# Configure the folder to save uploaded files
app.config['UPLOAD_FOLDER'] = 'cache/uploads/'  

@app.route('/')
def upload_form():
    return render_template("index.html")

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({
            "message": "File uploaded successfully",
            "filename": file.filename,
            "file_path": filepath
        }), 200

    return jsonify({"error": "Unknown error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)