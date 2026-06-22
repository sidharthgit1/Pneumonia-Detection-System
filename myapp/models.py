from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

class Doctor(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    contact = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50)
    place = models.CharField(max_length=15)
    pin = models.CharField(max_length=6)
    post = models.CharField(max_length=30)
    photo = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    contact = models.CharField(max_length=10)
    palce = models.CharField(max_length=15)
    pin = models.CharField(max_length=6)
    post = models.CharField(max_length=30)
    photo = models.CharField(max_length=200)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Feedback(models.Model):
    date = models.DateField()
    feedback = models.CharField(max_length=150)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Review(models.Model):
    date = models.DateField()
    feedback = models.CharField(max_length=150)
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    DOCTOR = models.ForeignKey(Doctor, on_delete=models.CASCADE,default='')

class Schedule(models.Model):
    date = models.DateField()
    from_time = models.CharField(max_length=150)
    to_time = models.CharField(max_length=150)
    slot = models.BigIntegerField(default="0")
    status=models.CharField(max_length=200)
    DOCTOR = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Appointment(models.Model):
    date = models.DateField()
    tocken=models.BigIntegerField(default="0")
    SCHEDULE = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Detection(models.Model):
    date = models.DateField()
    file = models.CharField(max_length=200)
    result=models.CharField(max_length=200)
    APPOINTMENT = models.ForeignKey(Appointment, on_delete=models.CASCADE)

