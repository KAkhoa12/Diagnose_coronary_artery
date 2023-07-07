import joblib

def predict_heart_disease(patient_features):
    # Load mô hình đã được huấn luyện
    model = joblib.load('path/to/saved_model.joblib')

    # Thực hiện dự đoán trên đặc trưng của bệnh nhân
    prediction = model.predict([patient_features])

    # Trả về kết quả dự đoán (0: không bị bệnh, 1: bị bệnh)
    return prediction[0]
