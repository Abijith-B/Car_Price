🚗 Car Price Prediction (Flask Project)
💰 Machine Learning Based Car Price Prediction Web App

A full-stack Car Price Prediction Web Application built using Flask and deployed on Railway.
This application predicts the resale price of a car based on user inputs such as year, fuel type, transmission, seller type, kilometers driven, and more.

The prediction is powered by a trained Random Forest Regression model.


🌐 Live Demo

🔗 https://web-production-23a82.up.railway.app/


Sample Vedio

![Uploading Car_pred vedio.gif…]()


📌 Features

✅ Predict car resale price instantly
✅ Machine Learning model integration (Random Forest Regressor)
✅ Clean and responsive user interface
✅ Real-time prediction results
✅ Flask backend processing
✅ Model saved using Pickle (rfr_model.pkl)
✅ Deployed and hosted on Railway

🛠️ Tech Stack

Frontend: HTML, CSS, Bootstrap

Backend: Flask

Machine Learning: Scikit-learn (Random Forest Regressor)

Model Storage: Pickle (.pkl file)

Deployment: Railway

📊 How It Works

1️⃣ User enters car details in the form
2️⃣ Flask processes the input data
3️⃣ Data is transformed into model-ready format
4️⃣ The trained Random Forest model predicts the price
5️⃣ Predicted price is displayed on the webpage

📂 Project Structure
Car_Price-main/
│
├── app.py               # Main Flask application
├── rfr_model.pkl        # Trained ML model
├── requirements.txt     # Project dependencies
├── Procfile             # Railway deployment file
├── runtime.txt          # Python runtime version
└── templates/           # HTML templates

⚙️ Local Setup Instructions
1️⃣ Clone the Repository
git clone <YOUR_GITHUB_REPO_LINK>
cd Car_Price-main
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

(Mac/Linux)

source venv/bin/activate
3️⃣ Install Required Dependencies
pip install -r requirements.txt
4️⃣ Run the Flask App
python app.py

Now open your browser and go to:

http://127.0.0.1:5000/
🚀 Deployment

This project is deployed using Railway with:

Procfile for web process configuration

runtime.txt for Python version

Automatic dependency installation via requirements.txt
