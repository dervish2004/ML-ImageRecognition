from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model import get_yolo_predictions
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='../frontend')
CORS(app)

# Define directories for uploads and outputs
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), 'outputs')

# Create the directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Serve the main page
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files from the frontend folder
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# New route to serve uploaded images
@app.route('/uploads/<path:filename>')
def serve_uploaded_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# New route to serve output images
@app.route('/outputs/<path:filename>')
def serve_output_image(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)

@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to handle image uploads, return predictions, and save files.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return jsonify({"error": "Invalid file type"}), 400

    # Secure the filename to prevent directory traversal attacks
    filename = secure_filename(file.filename)
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    
    # Save the original uploaded file
    file.save(upload_path)
    
    # Read the image data from the saved file for prediction
    image_bytes = open(upload_path, 'rb').read()
    predictions = get_yolo_predictions(image_bytes)
    
    output_filename = None
    if predictions:
        # Load the image to draw bounding boxes on
        img = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        
        for p in predictions:
            box = p['box']
            cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
            label = f"{p['class']}: {p['confidence']:.2f}"
            cv2.putText(img, label, (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        output_filename = f"output_{filename}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        cv2.imwrite(output_path, img)

    return jsonify({
        "predictions": predictions, 
        "input_filename": filename, 
        "output_filename": output_filename
    })

if __name__ == '__main__':
    app.run(debug=True)