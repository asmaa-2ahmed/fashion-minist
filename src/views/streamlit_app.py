import streamlit as st
import requests
import time
from PIL import Image
import matplotlib.pyplot as plt

# Constants - Update these to match your FastAPI app
API_URL = "http://127.0.0.1:8000"  # Your FastAPI server address
CLASS_NAMES = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']
   # Emoji mapping for each class
emoji_map = {
        'T-Shirt': '👕',
        'Trouser': '👖', 
        'Pullover': '🧥',
        'Dress': '👗',
        'Coat': '🧥',
        'Sandal': '👡',
        'Shirt': '👔',
        'Sneaker': '👟',
        'Bag': '👜',
        'Ankle Boot': '👢'
    }
    

# Page Configuration
st.set_page_config(
    page_title="Fashion Classifier", 
    page_icon="🛍️", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    :root {
        --primary: #6a1b9a;
        --secondary: #9c27b0;
        --accent: #e1bee7;
    }
    
    .auth-container {
        background: linear-gradient(135deg, #f9f0ff 0%, #e8d4ff 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(106, 27, 154, 0.1);
        margin-bottom: 2rem;
    }
    
    .fashion-item {
        display: inline-block;
        margin: 0.3rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        background: #f3e5f5;
        color: #4a148c;
        font-weight: 500;
    }
    
    .stProgress > div > div > div {
        background: linear-gradient(90deg, var(--primary) 0%, var(--secondary) 100%);
    }
</style>
""", unsafe_allow_html=True)

# Authentication Functions
def check_api_key(api_key):
    """Verify API key with backend"""
    try:
        response = requests.get(
            f"{API_URL}/",
            headers={"X-API-Key": api_key}
        )
        return response.status_code == 200
    except Exception:
        return False

# Initialize session state
if 'auth' not in st.session_state:
    st.session_state.auth = {
        'is_authenticated': False,
        'api_key': None,
        'login_time': None
    }

# ======================
# Authentication Section
# ======================
if not st.session_state.auth['is_authenticated']:
    # Main title and description
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='color: #6a1b9a;'>🛍️ Fashion Classifier</h1>
        <p style='color: #616161; font-size: 1.1rem;'>
            Upload clothing images for AI-powered classification
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # Auth card with better spacing and visual hierarchy
    with st.container():
               
        # API Key Input with clear instructions
        api_key = st.text_input(
            "**API Key**",
            type="password",
            placeholder="paste your key here",
            help="Your unique access key for the Fashion Classifier API",
        )
        
        # Submit button with loading state
        auth_button = st.button(
            "**Continue to Classifier** →",
            use_container_width=True,
            type="primary",
            key="auth_button"
        )
                
        st.markdown("</div>", unsafe_allow_html=True)  # Close card container
        
        # Authentication logic
        if auth_button:
            if not api_key:
                st.warning("Please enter your API key", icon="⚠️")
            else:
                with st.spinner("Verifying API key..."):
                    if check_api_key(api_key):
                        st.session_state.auth = {
                            'is_authenticated': True,
                            'api_key': api_key,
                            'login_time': time.time()
                        }
                        st.rerun()
                    else:
                        st.error("""
                        **Invalid API Key**  
                        The key you entered doesn't appear to be valid. Please:
                        - Double-check for typos
                        - Ensure you're using the correct key
                        - Contact support if problems persist
                        """, icon="🚨")
        # Help section with black text
        st.markdown("""
        <div style='
            margin-top: 1.5rem;
            padding: 1rem;
            background: #f9f0ff;
            border-radius: 8px;
            font-size: 0.9rem;
            color: #000000;  /* Black text */
        '>
            <p style='margin-bottom: 0.5rem; color: #000000;'>ℹ️ <strong>Where to find your API key:</strong></p>
            <ul style='margin-top: 0; padding-left: 1.2rem; color: #000000;'>
                <li>Check the "API_SECRET_KEY" from your .env file</li>
                <li>Contact your administrator</li>
                <li>Visit the developer portal</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Supported items section with black text
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center;'>
        <h3>🛍️ Supported Fashion Items</h3>
        <p style='color: #f3e5f5;'>Our classifier recognizes these clothing categories:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Display categories in a responsive grid with black text
    cols = st.columns(4)
    for i, item in enumerate(CLASS_NAMES):
        with cols[i % 4]:
            st.markdown(f"""
            <div style='
                padding: 0.5rem;
                margin: 0.3rem 0;
                background: #f3e5f5;
                border-radius: 8px;
                text-align: center;
                font-size: 0.9rem;
                color: #000000;  /* Black text */
            '>
                {item.replace('_', ' ')}
            </div>
            """, unsafe_allow_html=True)
else:
    # ======================
    # Main Application
    # ======================
    
    # Show brief success message
    if time.time() - st.session_state.auth['login_time'] < 3:
        with st.empty():
            st.success("Authentication successful! Welcome to Fashion Classifier", icon="🎉")
            time.sleep(1)
            st.empty()
    
    # Sidebar Navigation
    with st.sidebar:
        
        st.markdown("### Supported Items")
        # Display each item with emoji
        for item in CLASS_NAMES:
            display_name = item.replace('_', ' ')
            emoji = emoji_map.get(display_name, '👚')  # Default emoji if not found
            st.markdown(f"<div style='margin: 0.5rem 0;'>{emoji} {display_name}</div>", 
                    unsafe_allow_html=True)
        
        st.markdown("---")
        if st.button("🔒 Lock Classifier", key="lock_button"):  # Unique key added
            st.session_state.auth['is_authenticated'] = False
            st.rerun()
    
    # Main Content Area
    st.markdown("<h1 style='color: #6a1b9a;'>🛍️ Fashion Classifier</h1>", unsafe_allow_html=True)
    
    # File Uploader
    uploaded_file = st.file_uploader(
        "Upload a fashion item image",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=False
    )
    

    # Only proceed if user has uploaded a file
    if uploaded_file:
        try:
            # Safely open and display image preview
            image = Image.open(uploaded_file)
            resized_image = image.resize((300, 300))
            st.image(resized_image, caption="Uploaded Image", use_container_width=False)
            
            # Reset the file pointer so we can re-read it later
            uploaded_file.seek(0)

        except Exception as e:
            st.error(f"Could not read the uploaded file as an image: {e}")
        else:
            if st.button("🧠 Predict Fashion Item"):
                with st.spinner("Classifying..."):
                    try:
                        # ✅ Read file bytes for sending to FastAPI
                        uploaded_file.seek(0)  # Just to be safe
                        file_bytes = uploaded_file.read()
                        
                        # Prepare multipart/form-data payload
                        files = {
                            "file": (uploaded_file.name, file_bytes, uploaded_file.type)
                        }

                        headers = {
                            "X-API-Key": st.session_state.auth["api_key"]
                        }

                        # Send POST request to FastAPI
                        response = requests.post(f"{API_URL}/predict", files=files, headers=headers)

                        # Process successful response
                        if response.status_code == 200:
                            result = response.json()
                            predicted_class = result.get("class_name")
                            confidence = result.get("confidence", 0.0)

                            emoji = emoji_map.get(predicted_class, "👗")

                            # Display styled result box
                            st.markdown(f"""
                                <div style='
                                    margin-top: 2rem;
                                    padding: 1rem;
                                    border-radius: 12px;
                                    background-color: #f3e5f5;
                                    color: #4a148c;
                                    text-align: center;
                                    font-size: 1.2rem;
                                '>
                                    <strong>Prediction:</strong> {emoji} <span style='font-size: 1.4rem;'>{predicted_class}</span><br>
                                    <strong>Confidence:</strong> {confidence:.2f}%
                                </div>
                            """, unsafe_allow_html=True)
                        
                        else:
                            # Report server error with details
                            st.error(f"Prediction failed. Status: {response.status_code}, Response: {response.text}")

                    except Exception as e:
                        st.error(f"Exception while contacting prediction API: {e}")
