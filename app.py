from flask import Flask, request, render_template
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        beds = int(request.form['beds'])
        baths = float(request.form['baths'])
        size = int(request.form['size'])
        zip_code = int(request.form['zip_code'])

        # Make prediction
        features = np.array([[beds, baths, size, zip_code]])
        prediction = model.predict(features)

        return render_template('index.html', prediction=round(prediction[0], 2))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
