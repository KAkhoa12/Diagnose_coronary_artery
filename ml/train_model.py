import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
from pathlib import Path

# Đọc dữ liệu từ file CSV
data = pd.read_csv('heart.csv')

# Tách features và target
X = data.drop('target', axis=1)
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình RandomForestClassifier
model = RandomForestClassifier()

# Huấn luyện mô hình trên tập huấn luyện
model.fit(X_train, y_train)

# Đánh giá mô hình trên tập kiểm tra
accuracy = model.score(X_test, y_test)
print("Độ chính xác của mô hình:", accuracy)
# Đường dẫn tới thư mục 'app'
current_dir = Path(__file__).resolve().parent

# Đường dẫn tới thư mục 'app'
app_dir = current_dir.parent / 'app'
# Lưu mô hình vào thư mục 'app'
dump(model, app_dir / 'saved_model.joblib')
# Lưu mô hình vào file
dump(model, 'saved_model.joblib')
