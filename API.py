from tensorflow import keras
from Feature_Extractor import extract_features
import numpy as np  # ✅ Add this import


# ------------------------------------------------------------------------

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    print("Extracting features from url...")
    url_features = extract_features(url)
    print(url_features)

    print("Making prediction...")

    # ✅ FIX: Convert to NumPy array before passing to model
    url_features_np = np.array([url_features])  # Shape: (1, 16)
    prediction = model.predict(url_features_np)

    i = prediction[0][0] * 100
    i = round(i, 3)
    print("There is", i, "% chance the URL is malicious!")

    return i


