const form = document.getElementById('image-upload-form');
const fileInput = document.getElementById('image-file');
const imagePreview = document.getElementById('image-preview');
const predictionsContainer = document.getElementById('predictions-container');
const predictionsList = document.getElementById('predictions-list');
const statusMessage = document.createElement('p');
form.parentNode.insertBefore(statusMessage, form.nextSibling);

// IMPORTANT: The backend API URL is the same.
const BACKEND_API_URL = 'predict';

form.addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (!file) {
        statusMessage.textContent = 'Please select a file.';
        return;
    }

    // Clear previous predictions and show a preview
    predictionsList.innerHTML = '';
    predictionsContainer.style.display = 'none';
    statusMessage.textContent = 'Preparing to upload...';

    // Show a preview of the uploaded image
    const reader = new FileReader();
    reader.onload = (e) => {
        imagePreview.src = e.target.result;
        imagePreview.style.display = 'block';
    };
    reader.readAsDataURL(file);

    // Prepare the form data to send to the backend
    const formData = new FormData();
    formData.append('file', file);

    // Send the image to the backend API
    try {
        statusMessage.textContent = 'Uploading and analyzing image... Please wait.';
        
        const response = await fetch(BACKEND_API_URL, {
            method: 'POST',
            body: formData,
        });

        // Check for specific HTTP errors
        if (response.status === 400) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Bad request. Check the file type.');
        }

        if (!response.ok) {
            throw new Error(`Server responded with status: ${response.status}`);
        }

        const data = await response.json();
        
        // Clear any previous output images
        const existingOutputImage = document.getElementById('output-image');
        if (existingOutputImage) {
            existingOutputImage.remove();
        }

        if (data.predictions && data.predictions.length > 0) {
            displayPredictions(data.predictions);
            statusMessage.textContent = `Analysis complete. Found ${data.predictions.length} object(s).`;

            // Display the output image from the server
            if (data.output_filename) {
                const outputImage = document.createElement('img');
                outputImage.id = 'output-image';
                outputImage.src = `http://127.0.0.1:5000/outputs/${data.output_filename}`;
                outputImage.alt = "Detected Objects";
                outputImage.style.maxWidth = '100%';
                outputImage.style.marginTop = '1em';
                predictionsContainer.appendChild(outputImage);
            }
        } else {
            predictionsContainer.style.display = 'block';
            predictionsList.innerHTML = '<li>No objects detected.</li>';
            statusMessage.textContent = 'Analysis complete. No objects were detected.';
        }

    } catch (error) {
        console.error('Error during prediction:', error);
        statusMessage.textContent = `Error: ${error.message}. Please try a different image.`;
        predictionsContainer.style.display = 'none';
    } finally {
        form.classList.remove('drag-over');
    }
});

function displayPredictions(predictions) {
    predictionsList.innerHTML = '';
    predictions.forEach(p => {
        const listItem = document.createElement('li');
        // Rounding confidence for better display
        const confidence = (p.confidence * 100).toFixed(2);
        listItem.textContent = `Object: ${p.class}, Confidence: ${confidence}%`;
        predictionsList.appendChild(listItem);
    });
    predictionsContainer.style.display = 'block';
}

fileInput.addEventListener('dragover', (event) => {
    event.preventDefault();
    form.classList.add('drag-over');
    statusMessage.textContent = 'Drop the image here!';
});

fileInput.addEventListener('dragleave', () => {
    form.classList.remove('drag-over');
    statusMessage.textContent = '';
});

fileInput.addEventListener('drop', (event) => {
    event.preventDefault();
    form.classList.remove('drag-over');
    fileInput.files = event.dataTransfer.files;
    fileInput.dispatchEvent(new Event('change'));
});

// Clear message on initial page load
document.addEventListener('DOMContentLoaded', () => {
    statusMessage.textContent = '';
});