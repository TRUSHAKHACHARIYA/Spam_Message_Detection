# 📨 **Spam Message Detection** 📱

Welcome to the **Spam Message Detection** project! 🚫📧 This application classifies messages as **Spam** or **Ham** (non-spam). Built with **FastAPI** and **scikit-learn**, this project features both a **backend API** and a **frontend** to offer a smooth user experience.

---

### 🚀 **What is it?**

This project uses machine learning to classify SMS messages as either **Spam** or **Ham**. With a user-friendly interface, users can simply type in a message and get a prediction about its authenticity, all thanks to **FastAPI** and a pre-trained machine learning model! 🤖

---

### 🛠️ **Technologies Used**

- **Backend**:  
  - FastAPI 🚀  
  - scikit-learn 🧠  
  - pandas 🧑‍💻  
  - joblib 🎯

- **Frontend**:  
  - HTML 🖥️  
  - CSS 🎨  
  - JavaScript ⚡

---

### 📥 **Installation Guide**

To get started with the **Spam Message Detection** app:

1. **Clone this repository**:
    ```bash
    git clone https://github.com/yourusername/spam-message-detection.git
    cd spam-message-detection
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the FastAPI backend**:
    ```bash
    uvicorn main:app --reload
    ```

5. Visit **`http://localhost:8000`** in your browser to start testing! ✨

---

### 🔄 **How It Works** 💡

1. **Data Preprocessing**:
    - We clean and prepare raw SMS data for model training. 🧹
    - Text is vectorized using **TF-IDF** for feature extraction.

2. **Model Training**:
    - A machine learning model (e.g., **Logistic Regression** or **Naive Bayes**) is trained to recognize spam messages. 🎓
    - The model is saved using **joblib** for future use.

3. **Frontend Interface**:
    - **HTML** form where users can type their messages. ✍️
    - **JavaScript** sends the message to the FastAPI backend for classification.

4. **Backend**:
    - The backend classifies the message as **Spam** or **Ham** and returns a result with confidence scores. 🏆

---

