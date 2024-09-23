from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the LSTM model
model = tf.keras.models.load_model('notebooks/lstm_sales_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json(force=True)
        
        # Ensure the input data is provided as a 2D array (batch size, time steps, features)
        input_data = np.array(data['input']).reshape((1, 1, len(data['input'])))
        
        # Make prediction using the loaded model
        prediction = model.predict(input_data)
        
        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction[0].tolist()})
    
    except KeyError as e:
        return jsonify({'error': f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
