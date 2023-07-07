import joblib

def load_model():
    # Đường dẫn tới file đã lưu của mô hình
    model_path = 'path_to_your_model_file.pkl'

    # Sử dụng joblib để tải mô hình từ file
    model = joblib.load(model_path)

    return model