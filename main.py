from fastapi import FastAPI, HTTPException, Depends, UploadFile
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

from src.config import APP_NAME, VERSION, API_SECRET_KEY
from src.inference import classify_image  # Assuming you have this function in src/inference.py

# Initialize the FastAPI app
app = FastAPI(title=APP_NAME, version=VERSION)

# Allow CORS for all origins
app.add_middleware(
   CORSMiddleware,  
   allow_origins=["*"],  # Allow all origins
   allow_methods=["*"],  # Allow all HTTP methods
   allow_headers=["*"],  # Allow all headers
)

# API key authentication setup
api_key_header = APIKeyHeader(name='X-API-Key')

# API key validation function
async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key

# Health check endpoint
@app.get('/', tags=['check'])
async def home(api_key: str = Depends(verify_api_key)):
    return {
        "app_name": APP_NAME,
        "version": VERSION,
        "message": "Up & running"
    }

# Prediction endpoint
@app.post('/predict', tags=['Prediction'])
async def classify(file: UploadFile, api_key: str = Depends(verify_api_key)):
    try:
        # Read file contents first
        contents = await file.read()

        # Check if file is empty
        if not contents:
            raise HTTPException(status_code=400, detail="Empty file provided")
        
        # Verify content type after reading
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")

        # Classify the image using the `classify_image` function (which should handle your model prediction)
        response = classify_image(contents)
        return response

    except HTTPException:
        raise
    except Exception as e:
        # Catch any other exceptions and return a 500 error
        raise HTTPException(status_code=500, detail=f"Image processing failed: {str(e)}")
