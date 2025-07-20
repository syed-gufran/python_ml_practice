# 🧠 Diabetes Prediction Web App

A simple machine learning web app built with **Streamlit** that predicts whether a person has diabetes using an SVM classifier.  

---

## 📁 Project Structure

```
.
├── web_app.py                  # Streamlit frontend
├── trained_model.sav          # Pre-trained SVM model
├── diabetes.csv               # Dataset used (optional)
├── diabetes_prediction.py     # Model training script (if needed)
├── diabetes prediction using SVM.ipynb # Jupyter notebook (exploratory)
└── README.md
```

---

## 🛠️ Setup Instructions

### ✅ 1. Clone the repository (or download all files)

```bash
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
```

Or move all files to a dedicated folder.

---

### ✅ 2. Create and activate a virtual environment (optional but recommended)

```bash
# Create a conda environment
conda create -n diabetes-env python=3.11 -y
conda activate diabetes-env
```

---

### ✅ 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install numpy pandas scikit-learn streamlit
```

---

### ✅ 4. Run the app

```bash
streamlit run web_app.py
```

After running, your default browser will open with the app at:

```
http://localhost:8501
```

---

## 📊 App Functionality

- Takes 8 health-related inputs (e.g., glucose, BMI, age).
- Predicts diabetes status using a trained **SVM model**.
- Instant feedback on prediction.

---

## 📂 Model Info

- Model file: `trained_model.sav`
- Built using: `scikit-learn` SVM
- Trained on: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## ✍️ Author

**Syed Gufran Hussain**  
Student, BBDITM  
AI/ML Enthusiast  
Project for academic and demo use.

---

## 📝 License

This project is open for educational use. Feel free to reuse, modify, or expand it!