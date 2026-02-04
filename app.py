from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('rfr_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Capture Inputs
        input_year = int(request.form['Year'])
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        fuel_type = int(request.form['Fuel_Type'])
        transmission = int(request.form['Transmission'])
        seller_type = int(request.form['Seller_Type'])
        owner = int(request.form['Owner'])

        # 2. Logic for Age (Critical for LinearRegression)
        # Linear models trained on 2018 data cannot process 2026.
        # We cap the calculation to the training year range.
        calc_year = min(input_year, 2018)
        car_age = 2018 - calc_year
        
        # 3. Categorical Encodings
        fuel_diesel = 1 if fuel_type == 1 else 0
        fuel_petrol = 1 if fuel_type == 0 else 0
        seller_individual = 1 if seller_type == 1 else 0
        transmission_manual = 1 if transmission == 0 else 0

        # 4. Construct EXACT 9-feature array 
        # Order must match the training set exactly:
        # [Present_Price, Kms_Driven, Owner, Age, Diesel, Petrol, Individual, Manual, Year]
        final_features = np.array([[
            present_price,
            kms_driven,
            owner,
            car_age,
            fuel_diesel,
            fuel_petrol,
            seller_individual,
            transmission_manual,
            calc_year # This is your 9th feature
        ]])

        prediction = model.predict(final_features)
        output = round(float(prediction[0]), 2)

        # 5. Logic Safeguard
        # If the model predicts more than the original price or negative, 
        # we apply a standard depreciation curve (85% value for new cars)
        if output > present_price or output < 0:
            output = round(present_price * 0.85, 2)

        return render_template('index.html', prediction_text=output)

    except Exception as e:
        return render_template('index.html', prediction_text=f"System Error: {str(e)}")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)