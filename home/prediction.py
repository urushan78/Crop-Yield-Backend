import pandas as pd
import numpy as np
import joblib
import json
from sklearn.preprocessing import StandardScaler

# def predict_production_rf(input_data):
#     # Load the trained model
#     model = joblib.load("random_forest_model_int_fin.pkl")

#     with open("scaling_params.json", "r") as file:
#         scaling_params = json.load(file)

#     scaled_inputs = []
#     for i in range(len(input_data)):
#         scaled_input = (input_data[i] - scaling_params["mean"][i]) / scaling_params["scale"][i]
#         scaled_inputs.append(scaled_input)

#     scaled_inputs = np.array(scaled_inputs).reshape(1, -1)
    
#     prediction = model.predict(scaled_inputs)

#     return prediction[0]

def predict_production_rf(input_data):
    model = joblib.load('tuned_rf_model.pkl')

    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    print('prediction:')
    print(prediction)
    
    return prediction[0]


# def scale_features(inputs):
#     data = pd.read_csv("final_dataset.csv")

#     features = data.drop(["Production(mt)"], axis=1)
#     target = data["Production(mt)"]

#     columns_to_scale = [
#         "Year",
#         "Latitude",
#         "Longitude",
#         "Precipitation(mm)",
#         "Temp(C)",
#         "Area(ha)",
#     ]

#     scaler = StandardScaler()
#     scaled_features = scaler.fit_transform(features[columns_to_scale].values)

#     scalable_features = np.array(inputs[0:6])
#     non_scalable_features = np.array(inputs[-5:])

#     scaled_inputs = scaler.transform(scalable_features.reshape(1, -1))
#     final_inputs = np.concatenate(
#         (
#             scaled_inputs.reshape(
#                 6,
#             ),
#             non_scalable_features,
#         )
#     ).reshape(1, -1)

#     return final_inputs


# def predict_production_gbt(year, latitude, longitude, precipitation, temperature, area,
#                        crop_barley, crop_maize, crop_millet, crop_paddy, crop_wheat):

#     #Load the trained model
#     model = joblib.load('gb_regressor.pkl')

#     scalable_features = np.array([year, latitude, longitude, precipitation, temperature, area]).reshape(1, -1)
#     non_scalable_features = np.array([crop_barley, crop_maize, crop_millet, crop_paddy, crop_wheat])

#     #Load csv file
#     data = pd.read_csv('final_dataset.csv')

#     #fit the scaler to the entire dataset
#     columns_to_scale = ['Year', 'Latitude', 'Longitude', 'Precipitation(mm)', 'Temp(C)', 'Area(ha)']
#     std_scaler = StandardScaler().fit(data[columns_to_scale].values)

#     #scale the inputs
#     scaled_features = std_scaler.transform(scalable_features)
#     scaled_features = scaled_features.reshape(6,)
#     final_input = np.concatenate((scaled_features, non_scalable_features)).reshape(1, -1)

#     prediction = model.predict(final_input)

#     return prediction[0]


# year, latitude, longitude, precipitation, temp_range, area,
#                         surface_pressure, specific_humidity, relative_humidity,
#                        crop_barley, crop_maize, crop_millet, crop_paddy, crop_wheat
