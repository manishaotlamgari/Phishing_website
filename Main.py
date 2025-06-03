

from API import get_prediction

# path to trained model
model_path = "/content/drive/MyDrive/Phishing/phishing/Phishing-Attack-Domain-Detection-main/models/Malicious_URL_Prediction.h5"

# input url
url ="https://www.rgukt.in/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)

