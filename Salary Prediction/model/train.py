import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib
import os

data = pd.read_csv("data/Salary Data.csv")

data.rename(columns={
    'Years of Experience': 'Experience',
    'Education Level': 'Education'
}, inplace=True)

data = data.dropna()

edu_encoder = LabelEncoder()
gender_encoder = LabelEncoder()

data['Education'] = edu_encoder.fit_transform(data['Education'])
data['Gender'] = gender_encoder.fit_transform(data['Gender'])

X = data[['Experience', 'Education', 'Gender']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")
joblib.dump(edu_encoder, "model/edu_encoder.pkl")
joblib.dump(gender_encoder, "model/gender_encoder.pkl")

print("Model trained with Kaggle dataset!")