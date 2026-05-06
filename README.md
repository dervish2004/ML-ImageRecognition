# 🧠 Machine Learning Image Recognition Service

A **production-ready image recognition and object detection service** powered by **YOLOv8 + Flask**, exposing a REST API and a simple web interface for real-time inference.

---

## 📌 Project Overview

This project provides an end-to-end **image recognition pipeline** that:

* Accepts image uploads via API or frontend
* Performs **object detection using YOLOv8 (PyTorch)**
* Returns annotated images with bounding boxes
* Stores both original and processed outputs for review

It is designed with a clean **client-server architecture**, making it suitable for deployment and extension into production systems.

---

## 🚀 Features

### 🔍 Object Detection

* Detects multiple objects in an image
* Uses **pre-trained YOLOv8 model (yolov8n.pt)**
* Outputs bounding boxes with class labels and confidence scores

### 🌐 RESTful API

* `/predict` endpoint for image inference
* Returns structured JSON response

### 💾 Persistent Storage

* Saves uploaded images (`/uploads`)
* Saves annotated results (`/outputs`)

### 🖼️ Visual Feedback

* Displays original image
* Displays processed image with bounding boxes

### ⚡ Lightweight Frontend

* Built with **Vanilla HTML, CSS, JavaScript**
* Simple upload and preview interface

---

## 🧰 Tech Stack

* **Backend Framework:** Flask (Python)
* **ML Model:** Ultralytics YOLOv8 (PyTorch)
* **Image Processing:** OpenCV
* **Frontend:** HTML, CSS, JavaScript (Vanilla JS)
* **Utilities:** Flask-CORS, Werkzeug

---

## 🏗️ Architecture

The system follows a modular **client-server architecture**:

```
frontend/  → User Interface Layer
backend/   → API + ML Processing Layer
```

### 📦 Backend Structure

```
backend/
│── app.py          # Flask server & API routes
│── model.py        # YOLOv8 inference logic
│── requirements.txt
│
├── weights/
│   └── yolov8n.pt  # Pre-trained model
│
├── uploads/        # Input images
├── outputs/        # Annotated images
```

### 🌐 Frontend Structure

```
frontend/
│── index.html      # UI interface
│── script.js       # API calls & DOM handling
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd backend
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start Flask Server

```bash
flask run
```

Server runs at:

```
http://127.0.0.1:5000
```

### Open Frontend

Open:

```
frontend/index.html
```

in your browser.

---

## 🔌 API Endpoints

### 📤 POST `/predict`

Uploads an image and returns detection results.

#### Request:

* Form-data:

  * `image`: input image file

#### Response:

```json
{
  "detections": [
    {
      "class": "person",
      "confidence": 0.92,
      "bbox": [x1, y1, x2, y2]
    }
  ],
  "input_image": "uploads/img.jpg",
  "output_image": "outputs/annotated_img.jpg"
}
```

---

## 📁 Project Workflow

1. User uploads image via frontend or API
2. Flask receives image and saves it in `/uploads`
3. YOLOv8 model performs inference
4. Bounding boxes are drawn using OpenCV
5. Annotated image saved in `/outputs`
6. JSON response returned to client

---

## 🖼️ Output Features

* Original image display
* Annotated image with:

  * Bounding boxes
  * Class labels
  * Confidence scores

---

## 🚀 Deployment

### Supported Platforms:

* Render
* Vercel (with serverless adaptation)
* Google Cloud Run
* AWS EC2

### Notes:

* No build step required
* Pure Python Flask backend

---

## 📌 Requirements

* Python 3.8+
* pip

---

## 📈 Future Improvements

* 🔥 Switch to YOLOv8-seg for segmentation
* ⚡ Optimize inference with ONNX/TensorRT
* 🌐 Deploy as cloud-based microservice
* 📊 Add real-time WebSocket streaming
* 📱 Mobile-friendly UI dashboard

---

## 📸 Screenshots

(Add screenshots of)

* Upload UI
* Detection output
* API response

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Dervish Talari**
