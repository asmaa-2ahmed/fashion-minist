## 🛍️ Fashion MNIST Classifier

Welcome to the **Fashion MNIST Classifier** — a fun and intuitive way to classify clothing items using deep learning! 👚👖👟

This project uses a trained neural network to recognize fashion items from the [Fashion MNIST dataset](https://github.com/asmaa-2ahmed/fashion-minist) and features a sleek **Streamlit** web interface for easy testing and interaction.

Whether you're an AI enthusiast or just curious about machine learning, this app is a great place to start! 🧠✨

---

## ⚙️ Installation & Setup

Follow these steps to get the project running locally on your machine:

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/fashion-minist.git
cd fashion-minist
```

### 2. **Create and Activate a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Set Up Environment Variables**
- Copy the example environment file:
  ```bash
  cp .env.example .env
  ```
- Open the `.env` file and **add your API key** (or keep the default if testing locally).

---

## 🚀 How to Run the App

To launch the Streamlit web interface, run:

```bash
streamlit run src/views/streamlit_app.py
```

This will automatically open the app in your browser. If it doesn’t, check your terminal for a local URL (usually something like `http://localhost:8501`).

---

## 🧑‍💼 How to Use the App

1. **Login First**  
   When the app opens, you'll be prompted to enter your **API key** — this is required to access the model. You can find this key in your `.env` file.

2. **Upload Your Image**  
   Once authenticated, you'll see an image uploader. Upload a **28x28 grayscale image** of a clothing item (or use one of the sample images provided in the `assets` folder).

3. **See the Magic! ✨**  
   The model will instantly analyze the image and display:
   - The predicted fashion category (e.g., *T-shirt*, *Sneaker*, *Bag*)
   - A confidence score
   - An optional visualization of the input

It’s that easy — no coding required!

---

## 🧠 How It Works

- The model is trained on the **Fashion MNIST** dataset.
- Input images are preprocessed and passed to a neural network built with TensorFlow/Keras.
- The trained model outputs probabilities for each of the 10 fashion classes.
- The class with the highest probability is selected and displayed in the app.

Behind the scenes, the app loads the model from the `assets` folder and handles the entire prediction pipeline in real time. 🚀

---

## 💡 Got Ideas or Feedback?

We’d love to hear from you!

If you:
- Found a bug 🐞
- Have a feature idea 🌟
- Want to contribute 💻

Feel free to open an issue or submit a pull request!  
Let’s make this better together 💬

---

## 📬 Contact

Have a question or suggestion?  
Open an issue on GitHub or reach out directly!
