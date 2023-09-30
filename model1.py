import os

import tensorflow

# Get the absolute path to the model file
model_file_path = os.path.abspath('aqi_prediction_model.h5')

# Load the model
model = tensorflow.keras.models.load_model(model_file_path)

