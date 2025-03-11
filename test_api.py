import requests
import json

url = "http://127.0.0.1:5000/inference/predict"  # Adjust if running on a different host/port

# Define input payload
data = [
    {
        "customerID": "1628-BIZYP",
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 85.0,
        "TotalCharges": 85.0,
        "Churn": 0
    }
]

# Send request
response = requests.post(url, json=data)

# Print response
print("Status Code:", response.status_code)
print("Response:", response.json())