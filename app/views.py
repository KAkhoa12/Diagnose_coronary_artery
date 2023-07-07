from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Patient
from .forms import PatientForm
import joblib
import os
# Create your views here.
def index(request):
   return render(request,'app/index.html')

def save_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cholesterol = request.POST.get('cholesterol')
        blood_pressure = request.POST.get('blood_pressure')
        blood_sugar = request.POST.get('blood_sugar')
        resting_ecg = request.POST.get('resting_ecg')
        max_heart_rate = request.POST.get('max_heart_rate')
        exercise_induced_angina = request.POST.get('exercise_induced_angina') == 'on'
        st_depression = request.POST.get('st_depression')
        st_slope = request.POST.get('st_slope')
        num_major_vessels = request.POST.get('num_major_vessels')
        thalassemia = request.POST.get('thalassemia')
        cp = int(request.POST.get('chest_pain'))
        # Tạo đối tượng Patient và lưu vào cơ sở dữ liệu
        patient = Patient(
            name=name,
            age=age,
            gender=gender,
            cholesterol=cholesterol,
            blood_pressure=blood_pressure,
            blood_sugar=blood_sugar,
            resting_ecg=resting_ecg,
            max_heart_rate=max_heart_rate,
            exercise_induced_angina=exercise_induced_angina,
            st_depression=st_depression,
            st_slope=st_slope,
            num_major_vessels=num_major_vessels,
            thalassemia=thalassemia,
            diagnosed=False,
            cp=cp
        )
        patient.save()

        age = int(request.POST.get('age')) 
        gender = 0 if request.POST.get('gender') == 'Female' else 1
        cholesterol = int(request.POST.get('cholesterol')) 
        blood_pressure = int(request.POST.get('blood_pressure')) 
        blood_sugar = 0 if request.POST.get('blood_sugar') == 'Normal' else 1
        resting_ecg = 0 if request.POST.get('resting_ecg') == 'Normal' else 1
        max_heart_rate = int(request.POST.get('max_heart_rate')) 
        exercise_induced_angina = True if request.POST.get('exercise_induced_angina') == 'on' else False
        st_depression = float(request.POST.get('st_depression')) 
        st_slope = 0 if request.POST.get('st_slope') == 'Upsloping' else 1 if request.POST.get('st_slope') == 'Flat' else 2
        num_major_vessels = int(request.POST.get('num_major_vessels')) 
        thalassemia = 0 if request.POST.get('thalassemia') == 'Normal' else 1 if request.POST.get('thalassemia') == 'Fixed Defect' else 2
        chest_pain = int(request.POST.get('chest_pain')) 
        patient_features = [
            age,
            gender,
            cholesterol,
            blood_pressure,
            blood_sugar,
            resting_ecg,
            max_heart_rate,
            exercise_induced_angina,
            st_depression,
            st_slope,
            chest_pain,
            num_major_vessels,
            thalassemia
        ]

        project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Đường dẫn tới file saved_model.joblib
        model_path = os.path.join(project_dir, 'app', 'saved_model.joblib')

        # Load mô hình đã được huấn luyện
        model = joblib.load(model_path)

        # Áp dụng mô hình để chuẩn đoán bệnh nhân
        prediction = model.predict([patient_features])

        # Xử lý kết quả dự đoán và trả về dữ liệu cho template
        if prediction:
            diagnosis = "Bệnh nhân có bệnh động mạch vành."
        else:
            diagnosis = "Bệnh nhân không có bệnh động mạch vành."

        context = {
            'diagnosis': diagnosis,
            'age': age,
            'gender': gender,
            'cholesterol': cholesterol,
            'blood_pressure': blood_pressure,
            'blood_sugar': blood_sugar,
            'resting_ecg': resting_ecg,
            'max_heart_rate': max_heart_rate,
            'exercise_induced_angina': exercise_induced_angina,
            'st_depression': st_depression,
            'st_slope': st_slope,
            'chest_pain': chest_pain,
            'num_major_vessels': num_major_vessels,
            'thalassemia': thalassemia
        }
        return render(request, 'app/result.html', context)


    return render(request, 'app/patient_form.html')

def list_patient(request):
    list = Patient.objects.all()
    return render(request, 'app/list_patient.html', {'patients': list})

def patient_detail(request, id):
    # Lấy đối tượng Patient dựa trên patient_id
    patient = Patient.objects.get(id=id)

    return render(request, 'app/patient_detail.html', {'patient': patient})


