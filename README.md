# Streamlit AutoML Dashboard

## 🚀 Overview
This **Streamlit AutoML Dashboard** allows users to upload a dataset, specify the target column, and choose between **classification** or **regression**. The system automatically:

- **Preprocesses data** (handles missing values, encodes categorical features)
- **Selects the best model** using hyperparameter optimization
- **Trains and optimizes the model**
- **Provides the trained model for download**

## 📌 Features
✅ Upload CSV file
✅ Choose target column
✅ Select Classification or Regression
✅ Auto-select best model using Optuna
✅ Train & Optimize the model
✅ Download the trained model

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/streamlit-automl-dashboard.git
cd streamlit-automl-dashboard
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚦 Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

## 📦 Dependencies
```txt
numpy==2.2.3
pandas==2.2.3
scikit-learn==1.4.1.post1
streamlit==1.42.1
joblib==1.4.2
optuna==3.6.1
altair==5.5.0  # Optional for data visualization
```

## 🎯 How It Works
1️⃣ **Upload CSV File** 📂  
2️⃣ **Select Target Column** 🎯  
3️⃣ **Choose Classification/Regression**  
4️⃣ **Train & Optimize Model** 🏋️  
5️⃣ **Download Trained Model** 📥  

## 🤖 Models Used
- **Classification:** Logistic Regression, RandomForest, SVM
- **Regression:** Linear Regression, RandomForest, SVR

## 📌 Example Output
The system selects the best model based on performance and optimizes it for the best accuracy or lowest error.

## 🔥 Contributing
Feel free to contribute by submitting **issues** or **pull requests**!

## 📜 License
This project is licensed under the MIT License.

---
🚀 **Built with ❤️ by Moundher Bouroumana**

