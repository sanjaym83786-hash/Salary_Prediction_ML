import joblib

def load_model():
    model = joblib.load("model/model.pkl")
    edu_encoder = joblib.load("model/edu_encoder.pkl")
    gender_encoder = joblib.load("model/gender_encoder.pkl")
    return model, edu_encoder, gender_encoder

def predict(model, edu_encoder, gender_encoder, exp, edu, gender):
    edu_encoded = edu_encoder.transform([edu])[0]
    gender_encoded = gender_encoder.transform([gender])[0]

    result = model.predict([[exp, edu_encoded, gender_encoded]])
    return int(result[0])