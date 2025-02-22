from flask import Flask, request, jsonify, send_file, render_template
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

def encrypt_message(image_path, message, output_path):
    """ Encrypts the message into the image and saves the result """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Invalid image path")

    height, width, _ = img.shape
    max_length = height * width  
    if len(message) > max_length:
        raise ValueError("Message is too long for this image!")

    message += chr(0)  
    d = {chr(i): i for i in range(256)}

    n, m = 0, 0
    for char in message:
        img[n, m, 0] = d[char]  
        m += 1
        if m >= width:
            m = 0
            n += 1

    cv2.imwrite(output_path, img)
    return output_path

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """ Handles image encryption via Flask API """
    if 'image' not in request.files or 'message' not in request.form:
        return jsonify({'error': 'Missing required fields'}), 400

    image = request.files['image']
    message = request.form['message']

    filename = secure_filename(image.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image.save(filepath)

    output_path = os.path.join(OUTPUT_FOLDER, 'encrypted_' + filename)

    try:
        encrypted_path = encrypt_message(filepath, message, output_path)
        return send_file(encrypted_path, as_attachment=True)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

def decrypt_message(image_path):
    """ Decrypts a message from the image """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Invalid image path")

    height, width, _ = img.shape
    c = {i: chr(i) for i in range(256)}

    message = ""
    n, m = 0, 0

    while True:
        char_code = img[n, m, 0]  
        if char_code == 0:  
            break
        message += c[char_code]
        m += 1
        if m >= width:
            m = 0
            n += 1

    return message

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """ Handles image decryption via Flask API """
    if 'image' not in request.files:
        return jsonify({'error': 'Missing required fields'}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    image.save(filepath)

    try:
        decrypted_message = decrypt_message(filepath)
        return jsonify({'message': decrypted_message})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
