from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
def load_model(model_filename):
    with open(model_filename, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Load your model
model = load_model('notebooks/model_23-09-2024-16-49-29-542195.pkl')

@app.route('/predict_sales', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json(force=True)
        
        # The expected input columns based on your model
        input_cols = ['Store', 'Day', 'Month', 'Year', 'DayOfWeek_1', 'DayOfWeek_2',
                      'DayOfWeek_3', 'DayOfWeek_4', 'DayOfWeek_5', 'DayOfWeek_6',
                      'DayOfWeek_7', 'Promo_0', 'Promo_1', 'StateHoliday_0', 'StateHoliday_a',
                      'StateHoliday_b', 'StateHoliday_c', 'StoreType_a', 'StoreType_b',
                      'StoreType_c', 'StoreType_d', 'Assortment_a', 'Assortment_b',
                      'Assortment_c']
        
        # Initialize an input array with zeros (default values)
        input_data = np.zeros(len(input_cols))

        # Populate the input array based on the received data
        input_data[0] = data['Store']    # 'Store'
        input_data[1] = data['Day']      # 'Day'
        input_data[2] = data['Month']    # 'Month'
        input_data[3] = data['Year']     # 'Year'

        # DayOfWeek: One-hot encoding based on the day of the week (1-7)
        input_data[4 + data['DayOfWeek'] - 1] = 1  # Adjust index for 'DayOfWeek_1' to 'DayOfWeek_7'

        # Promo: One-hot encoding for promo (0 or 1)
        input_data[11 + data['Promo']] = 1  # 'Promo_0' or 'Promo_1'

        # StateHoliday: One-hot encoding for state holidays
        state_holiday_map = {'0': 12, 'a': 13, 'b': 14, 'c': 15}
        input_data[state_holiday_map[data['StateHoliday']]] = 1  # 'StateHoliday_0', 'StateHoliday_a', etc.

        # StoreType: One-hot encoding for store types
        store_type_map = {'a': 16, 'b': 17, 'c': 18, 'd': 19}
        input_data[store_type_map[data['StoreType']]] = 1  # 'StoreType_a', 'StoreType_b', etc.

        # Assortment: One-hot encoding for assortment types
        assortment_map = {'a': 20, 'b': 21, 'c': 22}
        input_data[assortment_map[data['Assortment']]] = 1  # 'Assortment_a', 'Assortment_b', etc.

        # Reshape the input to match the model's expected input format
        prediction_input = input_data.reshape(1, -1)

        # Make prediction
        prediction = model.predict(prediction_input)

        # Return the prediction as a JSON response
        return jsonify({'sales_prediction': prediction.tolist()})
    
    except KeyError as e:
        return jsonify({'error': f"Missing key: {str(e)}"}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
