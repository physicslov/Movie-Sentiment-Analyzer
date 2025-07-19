# 🎬 Movie Sentiment Analyzer App (RNN Based with Streamlit)

This project is a web-based Movie Review Sentiment Analyzer built using **Streamlit**. It uses a **Simple Recurrent Neural Network (RNN)** to classify movie reviews as either **positive** or **negative**.

---

## 🚀 Features

- Accepts user-input movie reviews.
- Predicts sentiment using a trained Simple RNN model.
- Interactive UI built with Streamlit.
- Lightweight, fast, and easy to use.

---

## 🧠 Model Details

- **Model Type**: Simple RNN (Recurrent Neural Network)
- **Layers**:
  - Embedding Layer
  - SimpleRNN Layer
  - Dense (Fully Connected) Output Layer
- **Techniques Used**:
  - **Embedding Layer** to reduce sparse representation
  - **Early Stopping** to avoid overfitting
- **Accuracy**:
  - **Training Accuracy**: ~93%
  - **Testing Accuracy**: ~82%

---

## 🛠️ Tech Stack

- **Frontend & UI**: Streamlit
- **Machine Learning**: TensorFlow / Keras
- **NLP Techniques**:  Padding, Embedding
- **Language**: Python

---

## 📁 Project Structure

movie_sentiment_app/
  ├── model.h5 # Trained RNN model
  ├── app.py # Main Streamlit app
  ├── requirements.txt # List of Python dependencies
  ├── Movie_Review.ipynb # Main Training File
  └── README.md # Project documentation

yaml
Copy
Edit

---

## ▶️ How to Run the App

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/movie-sentiment-analyzer.git
   cd movie-sentiment-analyzer
Install Dependencies:
Create a virtual environment (optional but recommended), then:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit App:

bash
Copy
Edit
streamlit run app.py
Open the provided URL in your browser (usually http://localhost:8501)

📷 Screenshots
(Insert screenshots of your Streamlit UI here)

📌 Future Enhancements
Upgrade to LSTM or BERT for better accuracy

Add word cloud or sentiment score visualization

Support multiple languages

🤝 Credits
Created by Shivam jha as part of an NLP project using RNN and Streamlit.

