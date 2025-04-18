from PIL import Image
from io import BytesIO
import numpy as np
from .schemas import PredictionResponse
from .config import CLASS_NAMES, MODEL

def classify_image(image_bytes: bytes):
    try:
        # load and preprocess
        img = Image.open(BytesIO(image_bytes))
        if img.mode != "L":
            img = img.convert("L")
        img = img.resize((28, 28))
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # model prediction
        prediction = MODEL.predict(img_array, verbose=0)
        predicted_class = np.argmax(prediction, axis=-1)[0]
        predicted_name = CLASS_NAMES[predicted_class]

        # return all required fields
        response = {
            'class_index': int(predicted_class),
            'class_name': predicted_name,
            'confidence': float(prediction[0][predicted_class] * 100)
        }
        return PredictionResponse(**response)

    except Exception as e:
        # will be caught by your FastAPI endpoint and returned as a 500
        raise ValueError(f"Image processing failed: {str(e)}")
