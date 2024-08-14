# House-Price-Prediction-using-Flask

This repository contains a Flask web application for predicting house prices using a machine learning model. The application uses a RandomForestRegressor model trained on a dataset with features such as the number of bedrooms, bathrooms, size of the house, and zip code.

## Contents
app.py: The Flask application that serves the web interface and handles predictions.

final_dataset.csv: The dataset used for training the model.

house_price_model.pkl: The trained machine learning model, including preprocessing and model pipeline.

templates/index.html: The HTML template for the web form.

requirements.txt: A list of Python dependencies for the project.

## Setup
### Prerequisites
Ensure you have Python 3.6 or later installed. You will also need pip to install the necessary Python packages.

### Installation
1. Clone the Repository
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction

2. Create a Virtual Environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt
4. Running the Application
Start the Flask Server
python app.py
Access the Application

Open your web browser and go to http://127.0.0.1:5000/ to access the application.

## Usage
1. Input Data

Enter the number of bedrooms, bathrooms, size of the house (in sq ft), and zip code into the form fields.

2. Get Prediction

Click the "Predict" button to get the estimated house price based on the input data.

3. View Results

The predicted house price will be displayed on the same page.

## Model Evaluation
The model has been evaluated using cross-validation with 5 folds. The Mean Squared Error (MSE) for the model is printed during training, providing a measure of prediction accuracy.

## Troubleshooting
Error: AttributeError: 'OneHotEncoder' object has no attribute '_drop_idx_after_grouping'

Ensure that the version of scikit-learn used in your environment matches the version used during training. You can specify the version in requirements.txt.

FileNotFoundError

Ensure that the house_price_model.pkl file exists in the same directory as app.py. The file should be saved from the training script.

License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or issues, please contact digvijaylohar007@gmail.com.

## Example Snapshots
### Form Submission
![image](https://github.com/user-attachments/assets/6797c4f3-6e0a-4fa4-8623-d981ba80e200)


### Prediction Response

![image](https://github.com/user-attachments/assets/a2c5cbb5-830d-4ac4-be3e-86e255b3c8bc)

### GitHub Repository

https://github.com/DigvijayLohar/House-Price-Prediction-using-Flask.git
