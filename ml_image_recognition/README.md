# Machine Learning Image Recognition Service

A production-ready implementation of the Machine Learning Image Recognition Service project.

## Demo
- Live URL: (https://machine-learning-image-recognition.onrender.com)

## Features
- **Object Detection:** Identifies and classifies objects within an image using a pre-trained machine learning model.
- **RESTful API:** Provides a clean and accessible API endpoint (`/predict`) for image analysis.
- **Persistent Storage:** Stores uploaded images and their corresponding annotated outputs for review.
- **Visual Feedback:** Displays both the original uploaded image and the processed output with bounding boxes.

***

## 🚀 Live Demo
- **Live URL:** (https://machine-learning-image-recognition.onrender.com)

***

## 🛠️ Tech Stack
- **Framework:** Flask (Python)
- **Machine Learning:** Ultralytics YOLOv8 (PyTorch)
- **Image Processing:** OpenCV
- **Frontend:** Plain HTML, CSS, JavaScript (Vanilla JS)
- **Other:** `Flask-CORS`, `Werkzeug`

## Architecture
The project follows a **client-server architecture**.
- **`backend/`**: Contains the core Python application.
  - `app.py`: The main Flask application that defines API routes for predictions and serving files.
  - `model.py`: Encapsulates the machine learning logic, including loading the YOLOv8 model and performing inference.
  - `weights/`: Stores the pre-trained `yolov8n.pt` model.
  - `uploads/`: Stores the original images uploaded by the user.
  - `outputs/`: Stores the annotated images with bounding boxes.
- **`frontend/`**: Contains the client-side code.
  - `index.html`: The main user interface for image uploads.
  - `script.js`: Handles all user interactions, API calls, and displaying results on the webpage.

## Getting Started
### Prerequisites
- Python 3.8+
- `pip`

### Setup
```bash
# Navigate to the backend directory
cd backend

# Install dependencies
pip install -r requirements.txt
Environment Variables

This project does not require any environment variables for local development.

Run Locally

Bash
# Ensure you are in the backend directory
flask run
The server will start on http://127.0.0.1:5000. Open frontend/index.html in your web browser to use the application.

Build

Note: This project does not have a formal build step as it uses plain HTML, CSS, and JavaScript. The Python backend is run directly.

Deployment
Platform: Vercel (or any platform that supports Python serverless functions, like Render or Google Cloud Run)

Build Command: N/A (Python backend)

Output: N/A

API Endpoints
POST /predict: Uploads an image and returns a JSON response with object detection predictions, as well as the filenames for the stored input and output images.

Screenshots
(You need to add these yourself by taking screenshots of your working application.)

License
MIT

Author
Dervish Talari
