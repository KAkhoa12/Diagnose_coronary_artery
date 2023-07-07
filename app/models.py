from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    cholesterol = models.IntegerField()
    blood_pressure = models.IntegerField()
    blood_sugar = models.CharField(max_length=10)
    resting_ecg = models.CharField(max_length=50)
    max_heart_rate = models.IntegerField()
    exercise_induced_angina = models.BooleanField()
    st_depression = models.FloatField()
    st_slope = models.CharField(max_length=50)
    num_major_vessels = models.IntegerField()
    thalassemia = models.CharField(max_length=50)
    diagnosed = models.BooleanField(default=False)
    cp = models.IntegerField()

    def __str__(self):
        return self.name



