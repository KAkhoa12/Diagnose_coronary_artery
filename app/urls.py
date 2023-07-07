from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('patient-form', views.save_patient, name='save_patient'),
   path('patient-list', views.list_patient, name='list_patient'),
   path('patient-detail/<int:id>/', views.patient_detail, name='patient_detail'),
   # path('result/', views.result_view, name='result_view'),
]