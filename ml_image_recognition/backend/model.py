import torch
from ultralytics import YOLO
import io
import cv2
import numpy as np

# Load the YOLO model from the weights folder
# 'yolov8n.pt' is the nano version, which is smaller and faster
try:
    model = YOLO("weights/yolov8n.pt")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def get_yolo_predictions(image_bytes):
    """
    Runs YOLOv8 inference on an image and returns a list of detected objects.

    Args:
        image_bytes (bytes): The raw bytes of the image file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a detected object.
              Each dictionary contains 'class', 'confidence', and 'box' information.
              Returns an empty list if the model is not loaded or an error occurs.
    """
    if model is None:
        return []

    try:
        # Decode the image bytes into a NumPy array
        np_array = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        # Run inference on the image
        results = model(img)

        detections = []
        for result in results:
            for box in result.boxes:
                detections.append({
                    "class": result.names[int(box.cls[0])],
                    "confidence": float(box.conf[0]),
                    "box": box.xyxy[0].tolist() # Bounding box coordinates
                })
        return detections
    except Exception as e:
        print(f"Error during inference: {e}")
        return []