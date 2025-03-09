from flask import Blueprint, request, jsonify
import pandas as pd
import traceback

# Define blueprint
inference_blueprint = Blueprint('inference', __name__)

@inference_blueprint.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.get_json()
        
        # Validate input
        if not isinstance(data, list):
            return jsonify({"error": "Input should be a list of records"}), 400
        
        # Convert to DataFrame
        df = pd.DataFrame(data)
        
        # Check if all required features are present
        missing_features = [col for col in MODEL_FEATURE if col not in df.columns]
        if missing_features:
            return jsonify({"error": f"Missing features: {missing_features}"}), 400
        
        # Run inference
        predictions = inference(df)
        
        # Return predictions
        return jsonify({"predictions": predictions.tolist()})
    
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500